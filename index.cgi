#!/usr/bin/perl
#print "Content-type: text/html;\n\n";print "<br>"; 

use utf8;

chdir('./cgi_system/admin/');


if(Windows_check()) {
	chdir(GetScriptPath($0));
}

sub	Windows_check
{
	# IIS,PWS(NT/95)対策
	$www_server_os = $^O;
	# Win98 & NT(SP4)対策
	if($www_server_os eq "") {
		$www_server_os= $ENV{'OS'};
	}
	# AnHTTPd/Omni/IIS 対策
	if($ENV{'SERVER_SOFTWARE'} =~ /AnWeb|Omni|IIS\//i) {
		$www_server_os= 'win';
	}
	# Win Apache 対策
	if($ENV{'WINDIR'} ne "") {
		$www_server_os= 'win';
	}
	if($www_server_os=~ /win/i) {
		return(1);
	}
	return(0);
}

sub	GetScriptPath {
	local($path) = @_;
	if($path =~ /[\:\/\\]/){
		$path =~ s/(.*?)[\/\\][^\/\\]+$/$1/;
	} else {
		$path = '.';
	}
	$path;
}




#	入力画面でのエラー表示。
$ERROR_DISPMODE = 1;

#=============================================================================
# ツリー
#
#	----+--[common]
#		|	jcode.pl
#		|	lib.pl
#		|	record.pl
#		|
#		+--[sessions]
#		|
#		+--[data]
#		|
#		+--[files]
#		+--[sys_image]
#		+--[item_image]
#		+--[item_image]
#		|
#		+--[adminreg]--[templates]
#						adminreg.cgi
#		+--[新しく作るcgi]
#=============================================================================

%File_NameList = (
	"errormsg"		=> "",												# □
	"nonname"		=> "",												# □
	);


#
# テンプレートファイルマトリクス
#
#	 mode 					テンプレートファイル
%temp_file = (
	"errormsg"					=> "error.html",				# 
	"item_list"					=> "item_list.html",			# 
	"item_add"					=> "item_list.html",			# 
	"item_add_cart"				=> "cart.html",					# 
	"item_mod_cart"				=> "item_list.html",			# 
	"item_mod"					=> "item_list.html",			# 
	"item_cart"					=> "cart.html",					# 
	"item_contact"				=> "contact_complete.html",		# 
);

%MODE = (
#	モード名				関数名				関数日本語		管理者区別(1:管理者 0:一般)			次モード
	"item_list"			=> [\&item_list			,'商品'				,0							,'item_list'			],	#
	"item_add"			=> [\&item_add			,'商品'				,0							,'item_add2'			],	#
	"item_add_cart"		=> [\&item_add			,'商品'				,0							,'item_add2'			],	#
	"item_mod_cart"		=> [\&item_add			,'商品'				,0							,'item_add2'			],	#
	"item_mod"			=> [\&item_list			,'商品'				,0							,'item_list'			],	#
	"item_cart"			=> [\&item_cart			,'商品'				,0							,'item_cart'			],	#
	"item_contact"		=> [\&item_contact		,'FORM'				,0							,'item_contact'			],	#
	"item_price"		=> [\&SyncscPrice		,'FORM'				,0							,'item_price'			],	#
);


#=============================================================================
#
#=============================================================================

$TEMPHTML_OUT			= 1;					# 1:データ置き換えモード	0:テンプレート吐き出しモード   [[--]]を生出力
# チェック方式
#	telhandy,tel,handyphone,fax,zip,ascii,kana,hira,minus,strnumeric,numeric,float,comma,alphanumeric,email,url,date,time,upfile,length,range,
#	指定無しでなし
#	複数は<>区切り
# 入力文字数最小
#	チェック方式のlength指定のとき有効
# 入力文字数最大
#	チェック方式のlength指定のとき有効
# 未記入
#	0;未記入可能　1:未記入不可
# 変換方式
#	||区切りでパラメータ
#	zip||郵便番号3名||郵便番号4名||郵便番号3-郵便番号4名		郵便番号3,郵便番号4から郵便番号3-郵便番号4の相互変換
#	date||年名||月名||日名||年/月/日名							年,月,日から年/月/日の相互変換
#	tel||tel1名||tel2名||tel3名||tel1-tel2-tel3名				tel1,tel2,tel3からtel1-tel2-tel3の相互変換
#	time||時名||分名||時:分名									時,分から時:分の相互変換
#	br-lf	<BR>からＬＦの相互変換
#	lfdel	改行コード削除
#	tabdel	タブコード削除
#	xss		xss対策html<>&"'を無効化	xssは順番で xss<>br-lfで順番で記述してください反対になると<BR>まで変換されます
#	z2h		全角英数字を半角に
#	h2z		半角を全角英数字に
#	kz2h	全角カナを半角に
#	kh2z	半角カナを全角に
#	指定無しでなし
#	複数は<>区切り
# htmlタイプ(オプション定義しておいてＨＴＭＬ生成に通すと雛形を作るために・・)
# 	text
# 	radio
# 	checkbox
# 	select
# 	textarea
#	||区切りでhtmlパラメータ
#		text||20||30														入力幅||最大入力値
#		radio||表示名1\t値1||表示名2\t値2										選択1\t値||選択2\t値
#		checkbox||表示名1\t値1||表示名2\t値2									選択1\t値||選択2\t値
# 		textarea||4||30															縦幅||入力幅
# 		select1||指定なし||../data/file.txt||hensu1||hensu2||xxx_RECORD			指定なしのときの表記||ファイル名||表示名を定義している変数名 $なし||値を定義している変数名 $なし||値を定義している構造体名 @なし
# 		radio1||指定なし||../data/file.txt||hensu1||hensu2||xxx_RECORD			指定なしのときの表記||ファイル名||表示名を定義している変数名 $なし||値を定義している変数名 $なし||値を定義している構造体名 @なし
# 		checkbox1||指定なし||../data/file.txt||hensu1||hensu2||xxx_RECORD		指定なしのときの表記||ファイル名||表示名を定義している変数名 $なし||値を定義している変数名 $なし||値を定義している構造体名 @なし
# 		select2||指定なし||array変数名											指定なしのときの表記||選択リストの配列変数名　$なし　"表示名\t値"で定義
# 生成しない
#	フォーマット "000000"
#				  ||||||
#				  ++++++---
# 							前から1番目：新規入力		0:生成する 1:しない 2:修正入力時確認表示
# 							前から2番目：新規確認表示	
# 							前から3番目：修正入力		
# 							前から4番目：修正確認表示	
# 							前から5番目：削除確認表示	
# 							前から6番目：確認表示		
# JavaScriptチェック
#	1でJavaScript補助入力を行う	0:でしない

#####2006
# 横並で項目表示
#	1で項目を横並びで出力する
# ｺﾒﾝﾄ制御
#	生成しないフォーマットと同じ	0でコメント出力		1でコメント出力しない
# 前ｺﾒﾝﾄ
#	入力エリアの前にｺﾒﾝﾄを出す
# 後ｺﾒﾝﾄ
#	入力エリアの後にｺﾒﾝﾄを出す

#\―ソЫⅨ噂浬欺圭構蚕十申曾箪貼能表暴予禄兔喀媾彌拿杤歃濬畚秉綵臀藹觸軆鐔饅鷭偆砡
#↑の文字を使う場合 \を頭に入れてください


#
#	情報入力。
#
%MAIN_REQUIRED = (
#   input name=					入力順位	日本語名									未記入			横並		ｺﾒﾝﾄ制御	前ｺﾒﾝﾄ		後ｺﾒﾝﾄ
#	"order_name_sei"			,["100"		,"お名前"									,"1"			," "		,""			,""			,""		],	#	名前
#	"order_name_mei"			,["110"		,"お名前"									,"1"			,""			,""			,""			,""		],	#	名前
#	"order_post"				,["120"		,"郵便番号"									,"1"			,""			,""			,""			,"-"	],	#	郵便番号
#	"order_prefecture"			,["130"		,"都道府県"									,"1"			,""			,""			,""			,""		],	#	都道府県
#	"order_address1"			,["140"		,"市区町村"									,"1"			,""			,""			,""			,""		],	#	市区町村
#	"order_address2"			,["150"		,"番地・マンション名"						,"0"			,""			,""			,""			,""		],	#	番地・マンション名
#	"order_tel"					,["160"		,"電話番号"									,"1"			,""			,""			,""			,""		],	#	電話番号
#	"order_email"				,["170"		,"メールアドレス"							,"1"			,""			,""			,""			,""		],	#	メールアドレス
	"send_salon_id"				,["200"		,"パートナーID"								,"0"			,""			,""			,""			,""		],	#	パートナーID
	"send_name_sei"				,["210"		,"お名前"									,"1"			," "		,""			,""			,""		],	#	名前
	"send_name_mei"				,["220"		,"お名前"									,"1"			,""			,""			,""			,""		],	#	名前
	"send_name_sei_kana"		,["230"		,"お名前フリガナ"							,"1"			," "		,""			,""			,""		],	#	名前フリガナ
	"send_name_mei_kana"		,["240"		,"お名前フリガナ"							,"1"			,""			,""			,""			,""		],	#	名前フリガナ
	"send_post"					,["250"		,"郵便番号"									,"1"			,""			,""			,""			,"-"	],	#	郵便番号
	"send_prefecture"			,["260"		,"都道府県"									,"0"			,""			,""			,""			,""		],	#	都道府県
	"send_address1"				,["270"		,"市区町村"									,"1"			,""			,""			,""			,""		],	#	市区町村
	"send_address2"				,["280"		,"番地・マンション名"						,"0"			,""			,""			,""			,""		],	#	番地・マンション名
	"send_tel"					,["290"		,"電話番号"									,"1"			,""			,""			,""			,""		],	#	電話番号
	"send_email"				,["300"		,"メールアドレス"							,"1"			,""			,""			,""			,""		],	#	メールアドレス
	"send_email_check"			,["310"		,"メールアドレス"							,"1"			,""			,""			,""			,""		],	#	メールアドレス
);

%MAIN_CHECKED = (
#			チェック方式			入力文字数最小			入力文字数最大			変換方式			htmlタイプ						生成しない			JavaScriptチェック
#	"order_name_sei"			,["length"						,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	名前
#	"order_name_mei"			,["length"						,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	名前
#	"order_prefecture"			,["length"						,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	都道府県
#	"order_post"				,["length<>zip"					,"0"				,"50"			,"z2h<>xss<>lfdel<>tabdel"		,"text||20||30"				,"000000"			,"0"			],	#	郵便番号
#	"order_address1"			,["length"						,"0"				,"500"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	市区町村・番地・マンション名など
#	"order_address2"			,["length"						,"0"				,"500"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	市区町村・番地・マンション名など
#	"order_tel"					,["length<>tel"					,"0"				,"50"			,"z2h<>xss<>lfdel<>tabdel"		,"text||5||16"				,"000000"			,"0"			],	#	電話番号
#	"order_email"				,["length<>email"				,"0"				,"50"			,"z2h<>xss<>lfdel<>tabdel"		,"text||5||16"				,"000000"			,"0"			],	#	メールアドレス
	"send_salon_id"				,["length"						,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	パートナーID
	"send_name_sei"				,["length"						,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	名前
	"send_name_mei"				,["length"						,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	名前
	"send_name_sei_kana"		,["length<>kana"				,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	名前フリガナ
	"send_name_mei_kana"		,["length<>kana"				,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	名前フリガナ
	"send_prefecture"			,["length"						,"0"				,"50"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	都道府県
	"send_post"					,["length<>zip"					,"0"				,"50"			,"z2h<>xss<>lfdel<>tabdel"		,"text||20||30"				,"000000"			,"0"			],	#	郵便番号
	"send_address1"				,["length"						,"0"				,"500"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	市区町村・番地・マンション名など
	"send_address2"				,["length"						,"0"				,"500"			,"xss<>lfdel<>tabdel"			,"text||20||30"				,"000000"			,"0"			],	#	市区町村・番地・マンション名など
	"send_tel"					,["length<>tel"					,"0"				,"50"			,"z2h<>xss<>lfdel<>tabdel"		,"text||5||16"				,"000000"			,"0"			],	#	電話番号
	"send_email"				,["length<>email"				,"0"				,"50"			,"z2h<>xss<>lfdel<>tabdel"		,"text||5||16"				,"000000"			,"0"			],	#	メールアドレス
	"send_email_check"			,["length<>email"				,"0"				,"50"			,"z2h<>xss<>lfdel<>tabdel"		,"text||5||16"				,"000000"			,"0"			],	#	メールアドレス
);

%MAIN_OPTION	= (
#						入力説明文	オプションタグ、コメント
#	"holiday"		,[ "",	qq|<a href="#" onclick="javascript:OpenWinCal(document.mform.holiday, 'mform.holiday');return false;"><img src="./cgi_image/images/cal_icon.gif" border=0></a>　<input type="button" value="クリア" onClick="TextClear(document.mform.holiday);" class="BtnGrayStyle02">|	]	,#"郵便番号",
);

%MAIN_OPTION_EX	= (
#						入力タグ制御文(disabled style)			checkbox,radio改行指定
#	"holiday_year"		,[ " class=\"w10\"  onChange=\"return day_dispctl(document.mform.holiday_year,document.mform.holiday_month,document.mform.holiday_day)\"><OPTION VALUE=\"\"",										""],
#	"holiday_month"		,[ " class=\"w10\"  onChange=\"return day_dispctl(document.mform.holiday_year,document.mform.holiday_month,document.mform.holiday_day)\"><OPTION VALUE=\"\"",										""],
#	"holiday_day"		,[ " class=\"w10\"  onChange=\"return day_dispctl(document.mform.holiday_year,document.mform.holiday_month,document.mform.holiday_day)\"><OPTION VALUE=\"\"",										""],
);


%LIST_SERACH = (
#									チェック方式		検索条件			文字形式		指定検索
#	"hyperlink_day"					,["DATE"			,"date"				,''			],
#	"hyperlink_url"					,["LIKE"			,"str"				,''			],
);

#	XSSエンコードされた文字列を戻す。
@DECODE_XSS = (
#	"order_name_sei"		,#	
#	"order_name_mei"		,#	
#	"order_prefecture"		,#	
#	"order_post"			,#	
#	"order_address1"		,#	
#	"order_address2"		,#	
#	"order_tel"				,#	
#	"order_email"			,#	
	"send_salon_id"			,#	
	"send_name_sei"			,#	
	"send_name_mei"			,#	
	"send_name_sei_kana"	,#	
	"send_name_mei_kana"	,#	
	"send_prefecture"		,#	
	"send_post"				,#	
	"send_address1"			,#	
	"send_address2"			,#	
	"send_tel"				,#	
	"send_email"			,#	
	"send_email_check"		,#	
);


#	一覧画面での検索条件を設定する。
%GROBAL_SESSION	= (
#		設定名				順序
		"order_items1",		[0],
		"order_items2",		[1],
		"order_items3",		[2],
		"order_items4",		[3],
		"order_items5",		[4],
		"p",				[5],
);

#	1度に注文できる注文数設定。
#	GROBAL_SESSIONの設定も変更が必要。
$ORDER_SETLIMIT = 1;


#=============================================================================
#
#=============================================================================


require '../public/basic.cgi';
require '../public/gconfig.cgi';
require '../spublic/setting.cgi';
require '../public/gcalender.cgi';
require '../public/cal.cgi';

require '../public/sendmail.cgi';
require '../public/mimew.pl';
require '../spublic/mail_setting.cgi';

use lib '../libpm';
use JSON;


#	初期設定。
$VAR{'method'} = $SETTING{'method'};

#	更新DBレコード構成指定。
@TARGET_RECORD = @ITEM_RECORD;

#	更新DBテキストファイルの保存場所指定。
$TARGETFILE = $SETTING{'itemfile'};


#	基本HTML保存先設定。
$SETTING{'inputhtml'}		 = 'input_tr.html';
$SETTING{'confirmhtml'}		 = 'confirm_tr.html';

$ERR_RETVAL = $FALSE; 

$USER_DISPLAY = $TRUE;

#	画面間保存(GROBAL_SESSION)に検索条件を追加する。
&GrobalSessionAddValue(\%GROBAL_SESSION);

&operation();


#
#	メイン処理。
#
sub		operation
{

	@MAIN_RECORD = ();
	%MAIN_SQLCREATE = ();

	@MEMBER_REC = ();

	#	基本設定。
#	$SQL_TABLE	= 'm_holiday';
#	$SQL_ORDER	= 'holiday_id';
#	$SQL_UNIQUE	= 'holiday_id';
#	$TARGET_TITLE = '休日マスタ';
#	$TARGET_VALUE = 'holiday_name';
#	$TARGET_VALUE_SEC = '';
	$SETTING{'list_limit'} = 5;

	#	スクリプト名を取得する。
	return $FALSE if (&GetScriptName(\$SETTING{'cgi_name'}) == $FALSE);
	$VAR{'cgi_url'} = "./$SETTING{'cgi_name'}";

	#	フォーム入力を取得する。
	&ReadParse(\%IN);

	if($IN{'submode'} eq ''){
		$IN{'submode'} = 'contact';
	}

	#	スマホ判定。
#	$smartphone_flg = &is_smartphone();
#	#$smartphone_flg = $TRUE;
#
#	if($smartphone_flg == $TRUE){
#		if($IN{'vm'} eq 'pc'){
#			$smartphone_flg = $FALSE;
#			$cart_data{'is_smartphone'} = $smartphone_flg;
#			&Make_Cookie(\%cart_data);
#		}else{
#			&Read_Cookie(\%COOKIE);
#			if($COOKIE{'is_smartphone'} ne ''){
#				$smartphone_flg = $COOKIE{'is_smartphone'};
#			}
#		}
#	}
#
#	if($IN{'vm'} eq 'sp'){
#		$smartphone_flg = $TRUE;
#		$cart_data{'is_smartphone'} = $smartphone_flg;
#		&Make_Cookie(\%cart_data);
#	}
##$smartphone_flg = $TRUE;
#


	#	モードが未設定の場合はデフォルトモードを設定する。
	$IN{'mode'}		= &EncodeXSS($IN{'mode'});
	$IN{'mode'} = 'item_list' if($IN{'mode'} eq '');

	#	入力文字列の不正をエスケープする。
	return $FALSE if (&InputEscape(\%IN) == $FALSE);

	#	ヘッダ・フッタボタンの生成。
	return $FALSE if (&MakeCommonButton(\%IN, \%VAR, \%SESSION) == $FALSE);

	#	設定情報追加。
	return $FALSE if (&Setting_Ex(\%IN, \%VAR, \%SESSION, \%MODE) == $FALSE);

	#	文字コードをプログラム内で利用するUTF8形式に変換する。
	return $FALSE if (&CharacterEncode_UTF8(\%IN, \%VAR, \%SESSION) == $FALSE);

	$VAR{'scrolltop'} = "0";

	$VAR{'gtag'}			 = &parse_template("../inc/gtag.php");
	$VAR{'meta'}			 = &parse_template("../inc/meta.php");
#	$VAR{'config'}			 = &parse_template("../inc/config.php");
	$VAR{'head'}			 = &parse_template("../inc/head.php");
#	$VAR{'include_slick'}	 = &parse_template("../inc/include_slick.php");
	$VAR{'header'}			 = &parse_template("../inc/header.php");
	$VAR{'footer'}			 = &parse_template("../inc/footer.php");

	$VAR{'gtag'} =~ s/\<\?\=DIR\?\>//g;
	$VAR{'meta'} =~ s/\<\?\=DIR\?\>//g;
	$VAR{'config'} =~ s/\<\?\=DIR\?\>//g;
	$VAR{'head'} =~ s/\<\?\=DIR\?\>//g;
	$VAR{'include_slick'} =~ s/\<\?\=DIR\?\>//g;
	$VAR{'header'} =~ s/\<\?\=DIR\?\>//g;
	$VAR{'footer'} =~ s/\<\?\=DIR\?\>//g;


	#	処理実行。
	return $FALSE if (&CallFunction($MODE{$IN{'mode'}}->[0]) == $FALSE);

	#	HTMLの出力。
	return $FALSE if (&ResultDisplay(\$VAR{'results'}) == $FALSE);

	#	正常終了。
	return $TRUE;

}


#
#	商品一覧画面
#
sub		item_list
{
	my(@datalist);
	my(@lines);
	my($rec_val);
	my($field_val);
	my($nums);
	my($tmplistcount);
	my(@tmplist);

	$VAR{'hidden'} = '';

	$IN{'p'}			= &EncodeXSS($IN{'p'});
	$IN{'submode'}		= &EncodeXSS($IN{'submode'});
	$IN{'mode'}			= &EncodeXSS($IN{'mode'});
	$IN{'gsession'}		= &EncodeXSS($IN{'gsession'});
	$IN{'area'}			= &EncodeXSS($IN{'area'});

	#	セッションIDが途切れた場合はクッキーを確認する。
	if($IN{'gsession'} eq ''){
		&Read_Cookie(\%COOKIE);
		$IN{'gsession'} = $COOKIE{'gsession'};
	}

	##	ページ間の保存値設定。
	#	ページ間の保存値の読み込み。
	&parsedata_read(\%ITEM, \%GROBAL_SESSION, \$SETTING{'gsession_dir'}, \$IN{'gsession'});

	#	データ(定義)がない場合はセッションデータを使用する。
	&_Replacegsession(\%GROBAL_SESSION, \%IN, \%ITEM);
#print "Content-type: text/html;\n\n";print "<br>"; 
#
##	DEBUG IKEDA
#for($infcnt=1; $infcnt <= $ORDER_SETLIMIT; $infcnt++){
#print "$infcnt";
#print "<>";
#print $IN{"order_items${infcnt}"};
#print "<br>";
#print "<br>";
#}
##	DEBUG IKEDA

	#	カート内の注文数を取得する。
	$VAR{'cart_count'} = 0;
	for($infcnt=1; $infcnt <= $ORDER_SETLIMIT; $infcnt++){
		$VAR{'cart_count'}++ if($IN{"order_items${infcnt}"} ne '');
	}
	$VAR{'cart_limit'} = $ORDER_SETLIMIT;


	if(($IN{'mode'} ne 'item_mod') && ($IN{'mode'} ne 'item_mod_cart')){
		$IN{'set_id'} = $VAR{'cart_count'} + 1;
	}

	##	カート追加ボタンの表示・非表示。
	$IN{'item_add_class'} = '';
	$IN{'item_add_cart_class'} = '';
	$IN{'item_mod_class'} = '';
	$IN{'item_mod_cart_class'} = '';


	#	注文更新処理。
	if(($IN{'mode'} eq 'item_add') || ($IN{'mode'} eq 'item_add_cart') || ($IN{'mode'} eq 'item_list')){

		$IN{'item_mod_class'} = 'display:none;';
		$IN{'item_mod_cart_class'} = 'display:none;';

	}elsif(($IN{'mode'} eq 'item_mod') || ($IN{'mode'} eq 'item_mod_cart')){

		$IN{'item_add_class'} = 'display:none;';
		$IN{'item_add_cart_class'} = 'display:none;';

	}

	#	エラーの場合はデータの読み込み処理は行わない。
	if($ERR_RETVAL != $TRUE){

		#	注文更新処理。
		if($IN{'mode'} eq 'item_mod'){

			#	セッションに保存された一時保存データを表示する。
			if($IN{"order_items$IN{'set_id'}"} ne ''){

				#	セッション構造化情報をカート情報と入力情報に分割する。
				@session_items = split('\|<=>\|', $IN{"order_items$IN{'set_id'}"});

				#	カート情報を取得する。
				@cart_items = split('\|\|', $session_items[0]);

				foreach $item (@cart_items){

					#	データが無い場合はスキップする。
					next if($item eq '');

					#	カート商品情報の取得。。
					@cart_item = split(':::', $item);

					#	IDを取得する。
					$VAR{'pro_id'} = $cart_item[0];
					$VAR{'pro_id'} =~ s/^pro_num_(.*)/$1/;

					#	商品設定数プルダウン用の値を取得する。
					$IN{"pro_num_$VAR{'pro_id'}"} = $cart_item[1];
				}

				#	注文主・送り先入力情報を取得する。
				$_cnt = 0;
				@input_items = split('::::', $session_items[1]);
				foreach $field (sort __by_inpseq keys %MAIN_REQUIRED) {
					$IN{$field} = $input_items[$_cnt];
					$_cnt++;
				}
			}

		#	追加の場合は注文主・送り先入力情報を「order_items1」から取得する。
		}else{

			#	セッションに保存された一時保存データを表示する。
			if($IN{"order_items1"} ne ''){

#				#	セッション構造化情報をカート情報と入力情報に分割する。
#				@session_items = split('\|<=>\|', $IN{"order_items1"});
#
#				#	注文主・送り先入力情報を取得する。
#				$_cnt = 0;
#				@input_items = split('::::', $session_items[1]);
#				foreach $field (sort __by_inpseq keys %MAIN_REQUIRED) {
#					$IN{$field} = $input_items[$_cnt];
#					$_cnt++;
#				}

				#	送り先はクリアする。
				$IN{'send_salon_id'}		= '';
				$IN{'send_name_sei'}		= '';
				$IN{'send_name_mei'}		= '';
				$IN{'send_name_sei_kana'}	= '';
				$IN{'send_name_mei_kana'}	= '';
				$IN{'send_prefecture'}		= '';
				$IN{'send_post'}			= '';
				$IN{'send_address1'}		= '';
				$IN{'send_address2'}		= '';
				$IN{'send_tel'}				= '';
				$IN{'send_email'}			= '';
				$IN{'send_email_check'}		= '';
				#$IN{'order_send_set'}		= '';
				$IN{'send_info'}			= '';
			}
		}
	}



	#	セッションに保存された一時保存データを表示する。
	if($IN{"order_items1"} ne ''){

		#	セッション構造化情報をカート情報と入力情報に分割する。
		@session_items = split('\|<=>\|', $IN{"order_items1"});

		#	注文主・送り先入力情報を取得する。
		$_cnt = 0;
		@input_items = split('::::', $session_items[1]);
		foreach $field (sort __by_inpseq keys %MAIN_REQUIRED) {
			$IN{"order_$field"} = $input_items[$_cnt];
			$_cnt++;
		}
	}

	#	商品一覧を生成する。
	$VAR{'item_list'} = &MakeItemList();

	#if(($IN{'mode'} ne 'item_mod') && ($IN{"order_items1"} ne '') || (($IN{'mode'} eq 'item_mod') && ($IN{'set_id'} ne '1'))){
	#if(($IN{'mode'} eq 'item_mod') && ($IN{'set_id'} ne '1')){
#	if(($IN{'set_id'} >= 2) || (($IN{'mode'} eq 'item_mod') && ($IN{'set_id'} ne '1')) || (($IN{'mode'} eq 'item_list') && ($IN{'set_id'} eq '') && ($IN{'order_items1'} ne ''))){
#		$VAR{'hidden'} .= qq|<input type="hidden" name="order_name_sei" value="$IN{'order_name_sei'}">\n|;
#		$VAR{'hidden'} .= qq|<input type="hidden" name="order_name_mei" value="$IN{'order_name_mei'}">\n|;
#		$VAR{'hidden'} .= qq|<input type="hidden" name="order_post" value="$IN{'order_post'}">\n|;
#		$VAR{'hidden'} .= qq|<input type="hidden" name="order_prefecture" value="$IN{'order_prefecture'}">\n|;
#		$VAR{'hidden'} .= qq|<input type="hidden" name="order_address1" value="$IN{'order_address1'}">\n|;
#		$VAR{'hidden'} .= qq|<input type="hidden" name="order_address2" value="$IN{'order_address2'}">\n|;
#		$VAR{'hidden'} .= qq|<input type="hidden" name="order_tel" value="$IN{'order_tel'}">\n|;
#		$VAR{'hidden'} .= qq|<input type="hidden" name="order_email" value="$IN{'order_email'}">\n|;
#	}

	$IN{'send_info'} =~ s/<br>/\n/gi;

	#	ラジオボタンの設定。
	$IN{'send_valid'} = 10010 if($IN{'send_valid'} eq '');
	$VAR{"send_valid_$IN{'send_valid'}"}= 'checked';

	#	注文更新処理。
	if(($IN{'mode'} eq 'item_list')){

		$IN{'btn_area_css'} = 'btn-area-double';

	}

	#	ナビゲータの背景色設定。
	if($IN{'set_id'} > 1){
		$VAR{'first_active'} = '';
		$VAR{'second_active'} = 'active';

		$IN{'btn_area_css'} = 'btn-area-triple';

	}else{
		$VAR{'first_active'} = 'active';
		$VAR{'second_active'} = '';
	}

	if(($IN{'mode'} eq 'item_mod') || ($IN{'mode'} eq 'item_mod_cart')){

		$IN{'btn_area_css'} = 'btn-area-single';

	}
	&MakeOutputHtml(\%IN, \%VAR, \$temp_file{$IN{'mode'}});

	#if(($IN{'mode'} ne 'item_mod') && ($IN{"order_items1"} ne '') || (($IN{'mode'} eq 'item_mod') && ($IN{'set_id'} ne '1'))){
	#if(($IN{'mode'} eq 'item_mod') && ($IN{'set_id'} ne '1')){

	if($IN{'set_id'} > 1){
		&TagDelete(\$VAR{'results'}, 'order_input_del', $TRUE);
		&TagDelete(\$VAR{'results'}, 'send_input_del', $FALSE);
		&TagDelete(\$VAR{'results'}, 'cart_button_del', $FALSE);

	}else{
		&TagDelete(\$VAR{'results'}, 'order_input_del', $FALSE);
		&TagDelete(\$VAR{'results'}, 'send_input_del', $TRUE);
		&TagDelete(\$VAR{'results'}, 'cart_button_del', $TRUE);
	}

	$VAR{'first_active'} = 'active';
	$VAR{'second_active'} = 'active';

#	if(($IN{'set_id'} >= 2) || (($IN{'mode'} eq 'item_mod') && ($IN{'set_id'} ne '1')) || (($IN{'mode'} eq 'item_list') && ($IN{'set_id'} eq '') && ($IN{'order_items1'} ne ''))){
#		&TagDelete(\$VAR{'results'}, 'order_input_del', $TRUE);
#		&TagDelete(\$VAR{'results'}, 'cart_button_del', $FALSE);
#	}else{
#		&TagDelete(\$VAR{'results'}, 'order_input_del', $FALSE);
#		&TagDelete(\$VAR{'results'}, 'cart_button_del', $TRUE);
#	}

	#	正常終了。
	return $TRUE;

}

#
#	カート追加処理。
#
sub		item_add
{
	my(@datalist);
	my(@lines);
	my($rec_val);
	my($field_val);
	my($nums);
	my($tmplistcount);
	my(@tmplist);

	$IN{'p'}			= &EncodeXSS($IN{'p'});
	$IN{'submode'}		= &EncodeXSS($IN{'submode'});
	$IN{'mode'}			= &EncodeXSS($IN{'mode'});
	$IN{'gsession'}		= &EncodeXSS($IN{'gsession'});
	$IN{'area'}			= &EncodeXSS($IN{'area'});

	#	注文2つ目以降は必須入力設定を変更する。
	if($IN{'set_id'} > 1){
		$MAIN_REQUIRED{'send_email'}[2] = '0';
		$MAIN_REQUIRED{'send_email_check'}[2] = '0';
	}

	#	入力値のエラーチェック。
	$ret = &item_check($ADDVIEW_MODE);
	if($ret) {
		if($IN{'mode'} eq 'item_add_cart'){
			$IN{'mode'} = "item_list";
		}
		$VAR{'program_title'}	= $MODE{$IN{'mode'}}->[1];
		$VAR{'mode_next'}	 	= $MODE{$IN{'mode'}}->[3];
		$ERR_RETVAL = $TRUE; 
		item_list();
		return $TRUE;
	}

	#	セッションIDが途切れた場合はクッキーを確認する。
	if($IN{'gsession'} eq ''){
		&Read_Cookie(\%COOKIE);
		$IN{'gsession'} = $COOKIE{'gsession'};
	}

	##	ページ間の保存値設定。
	#	ページ間の保存値の読み込み。
	&parsedata_read(\%ITEM, \%GROBAL_SESSION, \$SETTING{'gsession_dir'}, \$IN{'gsession'});

	#	データ(定義)がない場合はセッションデータを使用する。
	&_Replacegsession(\%GROBAL_SESSION, \%IN, \%ITEM);

#	if(($VAR{'send_name'} eq '') &&
#	   ($VAR{'send_name_kana'} eq '') &&
#	   ($VAR{'send_prefecture'} eq '') &&
#	   ($VAR{'send_post'} eq '') &&
#	   ($VAR{'send_address1'} eq '') &&
#	   ($VAR{'send_address2'} eq '') &&
#	   ($VAR{'send_tel'} eq '')){
#
#			$VAR{'send_name'}	 = $VAR{'order_name_sei'};
#			$VAR{'send_name_kana'}	 = $VAR{'order_name_mei'};
#			$VAR{'send_prefecture'}	 = $VAR{'order_prefecture'};
#			$VAR{'send_post'}		 = $VAR{'order_post'};
#			$VAR{'send_address1'}	 = $VAR{'order_address1'};
#			$VAR{'send_address2'}	 = $VAR{'order_address2'};
#			$VAR{'send_tel'}		 = $VAR{'order_tel'};
#
#	}


	#
	#	入力情報をセッションに保存する。
	#

	#	テーブル構造を取得する。
	return $FALSE if (&GetTableStructureList(\@MAIN_RECORD, \%SQLCONFIG, \%MAIN_SQLCREATE, 'm_product') == $FALSE);

	$dbh = &sqlwrap_db($SQLCONFIG{db_host},$SQLCONFIG{db_user},$SQLCONFIG{db_password},$SQLCONFIG{db_database});
	$sql_statement = qq| SELECT|
					.qq|    pro_id|
					.qq| FROM|
					.qq|    m_product|
					.qq| WHERE|
					.qq|    pro_valid = 10000|
					.qq| ORDER BY|
					.qq|    pro_sort|
					;
	$query = &sqlwrap_query($dbh,"$sql_statement");
	$nums = &sqlwrap_num_rows($query);
	for(my $num=0;$num < $nums;$num++) {
		$rec_val = sqlwrap_fetch_assoc($query);
		foreach $field_val (@MAIN_RECORD){
			${$field_val} = &Encode_UTF8($rec_val->{$field_val});
		}

		#	数量入力が数値である事を確認する。
		if(&Number_Check($IN{"pro_num_${pro_id}"})){

			#	0以上であれば処理する。
			if($IN{"pro_num_${pro_id}"} > 0){

				#	セッション登録形式にコンバートする。
				$set_item_key = qq|pro_num_${pro_id}:::$IN{"pro_num_${pro_id}"}|;
				push(@set_order_items, $set_item_key);
			}
		}
	}

	#	セッションにカート情報に追加する。
	if($#set_order_items >= 0){
		$order_item_data .= '||'.join('||', @set_order_items);
	}

	##	カート以外の入力情報を保存する。
	foreach $field (sort __by_inpseq keys %MAIN_REQUIRED) {
		push(@order_info_items, $IN{"$field"});
	}

	##	セッションに入力情報を追加する。
	#	更新処理。
	if($IN{'set_id'} ne ''){

		#	カート+|<=>|+入力情報のセットで保存する。
		$IN{"order_items$IN{'set_id'}"} = $order_item_data.'|<=>|'.join('::::', @order_info_items);

	#	追加処理。
	}else{

		#	1番から詰めて保存する。
		for($infcnt=1; $infcnt <= $ORDER_SETLIMIT; $infcnt++){
			if($IN{"order_items${infcnt}"} eq ''){

				#	カート+|<=>|+入力情報のセットで保存する。
				$IN{"order_items${infcnt}"} = $order_item_data.'|<=>|'.join('::::', @order_info_items);
				last;
			}
		}
	}

#$MAIN_REQUIRED{'send_email'}[2] = '0';
	#	ページ間の値を保存。
	$IN{'gsession'} = &parsedata_save(\%IN, \%GROBAL_SESSION, \$SETTING{'gsession_dir'}, \$SETTING{'gsession_length'});

	#	カートの金額取得用のパートナーIDを保存する。
	$IN{'send_salon_id'} = '' if($IN{'send_salon_id'} eq '');
	$VAR{'send_salon_id'} = $IN{'send_salon_id'};

	#	入力内容をクリアする。
	$IN{'send_salon_id'}		= '';
	$IN{'send_name_sei'}		= '';
	$IN{'send_name_mei'}		= '';
	$IN{'send_name_sei_kana'}	= '';
	$IN{'send_name_mei_kana'}	= '';
	$IN{'send_prefecture'}		= '';
	$IN{'send_post'}			= '';
	$IN{'send_address1'}		= '';
	$IN{'send_address2'}		= '';
	$IN{'send_tel'}				= '';
	$IN{'send_email'}			= '';
	$IN{'send_email_check'}		= '';
	$IN{'send_info'}			= '';

	#	商品数量のクリア。
	if(!open(DBDATA,"$TARGETFILE")) {
		&UserErrorDisplay($ERROR_FILE_READ,"$TARGETFILE","","");
	}
	@lines = <DBDATA>;
	close(DBDATA);
	foreach $ln (@lines) {

		$ln =~ s/\r\n$/\n/g;
		(@itemrec) = split(/\t/,$ln);
		${pro_id} = &Encode_UTF8($itemrec[0]);

		#	商品数の初期化。
		$IN{"pro_num_${pro_id}"} = 0;

	}

	if($IN{'mode'} eq 'item_add'){

		$IN{'mode'} = "item_list";
		$VAR{'program_title'}	= $MODE{$IN{'mode'}}->[1];
		$VAR{'mode_next'}	 	= $MODE{$IN{'mode'}}->[3];
		&item_list();

	}else{

		$IN{'mode'} = "item_cart";
		$VAR{'program_title'}	= $MODE{$IN{'mode'}}->[1];
		$VAR{'mode_next'}	 	= $MODE{$IN{'mode'}}->[3];
		&item_cart();

	}


	#	正常終了。
	return $TRUE;

}

#
#	カート画面
#
sub		item_cart
{
	my(%item_data);
	my(@datalist);
	my(@lines);
	my($rec_val);
	my($field_val);
	my($nums);
	my($tmplistcount);
	my(@tmplist);

	$VAR{'hidden'} = '';

	$IN{'p'}			= &EncodeXSS($IN{'p'});
	$IN{'submode'}		= &EncodeXSS($IN{'submode'});
	$IN{'mode'}			= &EncodeXSS($IN{'mode'});
	$IN{'gsession'}		= &EncodeXSS($IN{'gsession'});
	$IN{'area'}			= &EncodeXSS($IN{'area'});

	$VAR{'cart_limit'} = $ORDER_SETLIMIT;

	#	セッションIDが途切れた場合はクッキーを確認する。
	if($IN{'gsession'} eq ''){
		&Read_Cookie(\%COOKIE);
		$IN{'gsession'} = $COOKIE{'gsession'};
	}

	##	ページ間の保存値設定。
	#	ページ間の保存値の読み込み。
	&parsedata_read(\%ITEM, \%GROBAL_SESSION, \$SETTING{'gsession_dir'}, \$IN{'gsession'});

	#	データ(定義)がない場合はセッションデータを使用する。
	&_Replacegsession(\%GROBAL_SESSION, \%IN, \%ITEM);

	##	商品情報の取得。

	#	テーブル構造を取得する。
	return $FALSE if (&GetTableStructureList(\@MAIN_RECORD, \%SQLCONFIG, \%MAIN_SQLCREATE, 'm_product') == $FALSE);

	#	サロン情報。
	push(@MAIN_RECORD, 'sal_com_name');

	$IN{'send_salon_id'} = '' if($IN{'send_salon_id'} eq '');

	$dbh = &sqlwrap_db($SQLCONFIG{db_host},$SQLCONFIG{db_user},$SQLCONFIG{db_password},$SQLCONFIG{db_database});
	$sql_statement = qq| SELECT|
					.qq|    pro_id|
					.qq|   ,pro_code|
					.qq|   ,pro_name|
					.qq|   ,pro_image1|
					.qq|   ,pro_image2|
					.qq|   ,pro_image3|
					.qq|   ,(CASE WHEN agp_price_notax is null THEN pro_price_notax ELSE agp_price_notax END)  AS pro_price_notax|
					.qq|   ,(CASE WHEN agp_price is null THEN pro_price ELSE agp_price END)  AS pro_price|
					.qq|   ,pro_body|
					.qq|   ,pro_sort|
					.qq|   ,sal_com_name|
					.qq| FROM|
					.qq|    m_product|
					.qq| LEFT JOIN|
					.qq|    m_salon|
					.qq| ON|
					.qq|    sal_sales_id = '$VAR{'send_salon_id'}'|
					.qq| LEFT JOIN|
					.qq|    m_agency_price|
					.qq| ON|
					.qq|    agp_pro_id = pro_id|
					.qq|    AND|
					.qq|    agp_age_id = sal_age_id|
					.qq| WHERE|
					.qq|    pro_valid = 10000|
					.qq| ORDER BY|
					.qq|    pro_sort|
					;
	$query = &sqlwrap_query($dbh,"$sql_statement");
	$nums = &sqlwrap_num_rows($query);
	for(my $num=0;$num < $nums;$num++) {
		$rec_val = sqlwrap_fetch_assoc($query);
		foreach $field_val (@MAIN_RECORD){
			${$field_val} = &Encode_UTF8($rec_val->{$field_val});
		}

		$item_data{"$pro_id"}{'pro_name'}	 = $pro_name;	#	商品名
		$item_data{"$pro_id"}{'pro_price'}	 = $pro_price;	#	価格
		$item_data{"$pro_id"}{'pro_body'}	 = $pro_body;	#	本文
		$item_data{"$pro_id"}{'pro_image1'}	 = $pro_image1;	#	画像

	}

	#	合計金額の初期化。
	$VAR{'totalprice'} = 0;
	$VAR{'cart_count'} = 0;

	#	サロン名。
	$VAR{'sal_com_name'} = $sal_com_name;

	#	注文一覧を生成する。
	for($infcnt=1; $infcnt <= $ORDER_SETLIMIT; $infcnt++){

		#	注文商品リストHTMLの初期化。
		$VAR{'cart_list'} = '';

		#	セッション番号を取得する。
		$VAR{'session_list_id'} = $infcnt;

		if($IN{"order_items${infcnt}"} ne ''){

			$VAR{'item_count'} = 0;

			#	セッション構造化情報をカート情報と入力情報に分割する。
			@session_items = split('\|<=>\|', $IN{"order_items${infcnt}"});

			#	カート情報を取得する。
			$VAR{'subtotal'} = 0;
			$VAR{'subtotal_disp'} = 0;
			@cart_items = split('\|\|', $session_items[0]);
			foreach $item (@cart_items){

				#	データが無い場合はスキップする。
				next if($item eq '');

				$VAR{'item_count'}++;

				#	カート商品情報の取得。。
				@cart_item = split(':::', $item);
				$VAR{'pro_id'} = $cart_item[0];
				$VAR{'pro_id'} =~ s/^pro_num_(.*)/$1/;
				$VAR{'pro_num'} = $cart_item[1];
				$VAR{'pro_name'} = $item_data{"$VAR{'pro_id'}"}{'pro_name'};
				$VAR{'pro_price'} = $item_data{"$VAR{'pro_id'}"}{'pro_price'};
				$VAR{'pro_body'} = $item_data{"$VAR{'pro_id'}"}{'pro_body'};
				$VAR{'pro_image1'} = $item_data{"$VAR{'pro_id'}"}{'pro_image1'};

				#	小計算出。
				$VAR{'subtotal'} += ($VAR{'pro_price'} * $VAR{'pro_num'});

				#	金額カンマ。
				$VAR{'pro_price_disp'} = $VAR{'pro_price'};
				$VAR{'pro_price_disp'} =~ s/(\d{1,3})(?=(?:\d{3})+(?!\d))/$1,/g;

				#	商品画像。
				$VAR{'pro_image_disp'} = qq|$SETTING{'itemimgedir'}/$VAR{'pro_image1'}|;

				#	注文商品一覧生成。
				$VAR{'cart_list'} .= &parse_template('cart_list_tr.html');
			}

			#	注文主・送り先入力情報を取得する。
			$_cnt = 0;
			@input_items = split('::::', $session_items[1]);

			#	注文主データ取得。
			if($infcnt == 1){

				foreach $field (sort __by_inpseq keys %MAIN_REQUIRED) {
					$VAR{"$field"} = $input_items[$_cnt];
					$_cnt++;
				}
			}

			$VAR{'cart_count'}++ if($VAR{'subtotal'} > 0);
		}

		$VAR{'subtotal_disp'} = $VAR{'subtotal'};
		$VAR{'subtotal_disp'} =~ s/(\d{1,3})(?=(?:\d{3})+(?!\d))/$1,/g;

#		#	注文ブロックHTMLの生成。
#		if($VAR{'cart_list'} ne ''){
#			$VAR{'cart_item'} .= &parse_template('cart_input_flist_tr.html');
#			$VAR{'totalprice'} += $VAR{'subtotal'};
#		}
	}

	#	金額カンマ。
	$VAR{'totalprice'} =~ s/(\d{1,3})(?=(?:\d{3})+(?!\d))/$1,/g;

	if($VAR{'cart_item'} eq ''){
		$VAR{'cart_item'} = 'カートは空です。';
		$IN{'item_send_class'} = 'display:none;';
	}else{
		$IN{'item_send_class'} = '';
	}

	$IN{'send_memo_disp'} = $IN{'send_memo'};
	$IN{'send_memo_disp'} =~ s/\n/<br>/gi;

	#	全体表示のHTML生成。
	&MakeOutputHtml(\%IN, \%VAR, \$temp_file{$IN{'mode'}});

	#	正常終了。
	return $TRUE;

}


#
#	入力順の並び替え
sub	__by_inpseq
{

	#	昇順(先頭がソート番号)。
	$MAIN_REQUIRED{$a}[0] <=> $MAIN_REQUIRED{$b}[0];

}


#
#	商品一覧を生成する。
#
sub		MakeItemList
{
	my(@selectdata);
	my(@lines);
	my($nums);
	my($tmplistcount);
	my(@tmplist);
	my(@item_obj_list);
	my(@item_price_list);

	#	テーブル構造を取得する。
	return $FALSE if (&GetTableStructureList(\@MAIN_RECORD, \%SQLCONFIG, \%MAIN_SQLCREATE, 'm_product') == $FALSE);

	$dbh = &sqlwrap_db($SQLCONFIG{db_host},$SQLCONFIG{db_user},$SQLCONFIG{db_password},$SQLCONFIG{db_database});

	$sql_statement = qq| SELECT|
					.qq|    * |
					.qq| FROM|
					.qq|    m_product|
					.qq| ORDER BY|
					.qq|    pro_sort|
					;

	$query = &sqlwrap_query($dbh,"$sql_statement");
	$nums = &sqlwrap_num_rows($query);
	for(my $num=0;$num < $nums;$num++) {
		$rec_val = sqlwrap_fetch_assoc($query);
		foreach $field_val (@MAIN_RECORD){
			$VAR{$field_val} = $rec_val->{$field_val};
			$VAR{$field_val} = &Encode_UTF8($VAR{$field_val});
		}

		$key = $VAR{'pro_id'};
		$VAR{'key'} = $key;

		$VAR{'item_count'}++;

		#	金額カンマ。
		$VAR{'pro_price_disp'} = $VAR{'pro_price'};
		$VAR{'pro_price_disp'} =~ s/(\d{1,3})(?=(?:\d{3})+(?!\d))/$1,/g;

		#	商品画像。
		$VAR{'pro_image_disp'} = qq|$SETTING{'itemimgedir'}/$VAR{'pro_id'}|;

		#	数量プルダウンの設定。
		$VAR{"pro_num_$IN{'pro_num_'.$VAR{'pro_id'}}"}= 'selected';

		#	数量の表示設定。
		$VAR{'pro_number'}= $IN{'pro_num_'.$VAR{'pro_id'}};

		#	商品数の初期化。
		if($VAR{'pro_number'} eq ''){
			$VAR{'pro_number'} = 0;
		}

		$VAR{'pro_image1_disp'} = qq|$SETTING{'itemimgedir'}/$VAR{'pro_image1'}|;

		#	数量選択プルダウン生成。
		$VAR{'pro_num'}  = qq|<select name="pro_num_$VAR{'pro_id'}" id="pro_num_$VAR{'pro_id'}" onChange="javascript:colSetNumberTotal(document.mForm.pro_num_$VAR{'pro_id'});">|;
		$VAR{'pro_num'} .= &array_select_mk("select", '', '', 1, "$IN{'pro_num_'.$VAR{'pro_id'}}", \@SELECT_PRODUCT_NUMBER, '', '', '', ';');
		$VAR{'pro_num'} .= "</select>";

		$item_list .= &parse_template('item_list_tr.html');

#		#	数量プルダウンの設定のクリア。
#		$VAR{"pro_num_$IN{'pro_num_'.$VAR{'pro_id'}}"} = '0';
		push(@item_obj_list, "document.mForm.pro_num_".$VAR{'key'});
		push(@item_obj_price_list, "pro_price_$VAR{'key'}");
		push(@item_price_list, $VAR{'pro_price'});

	}

	$VAR{'item_obj_list'}  = join(',', @item_obj_list);
	$VAR{'item_obj_price_list'}  = join("','", @item_obj_price_list);
	$VAR{'item_price_list'}  = join(',', @item_price_list);

	#	結果セットを返す。
	return $item_list;

}


#
#	注文完了処理。
#
sub		item_contact
{
	my(%item_data);
	my(@datalist);
	my(@lines);
	my($rec_val);
	my($field_val);
	my($nums);
	my($tmplistcount);
	my(@tmplist);

	$VAR{'hidden'} = '';

	$IN{'p'}			= &EncodeXSS($IN{'p'});
	$IN{'submode'}		= &EncodeXSS($IN{'submode'});
	$IN{'mode'}			= &EncodeXSS($IN{'mode'});
	$IN{'gsession'}		= &EncodeXSS($IN{'gsession'});

	$VAR{'cart_limit'} = $ORDER_SETLIMIT;

	#	セッションIDが途切れた場合はクッキーを確認する。
	if($IN{'gsession'} eq ''){
		&Read_Cookie(\%COOKIE);
		$IN{'gsession'} = $COOKIE{'gsession'};
	}

	##	ページ間の保存値設定。
	#	ページ間の保存値の読み込み。
	&parsedata_read(\%ITEM, \%GROBAL_SESSION, \$SETTING{'gsession_dir'}, \$IN{'gsession'});

	#	データ(定義)がない場合はセッションデータを使用する。
	&_Replacegsession(\%GROBAL_SESSION, \%IN, \%ITEM);

	#	商品情報の取得。

	#	テーブル構造を取得する。
	return $FALSE if (&GetTableStructureList(\@MAIN_RECORD, \%SQLCONFIG, \%MAIN_SQLCREATE, 'm_product') == $FALSE);

	#	サロン情報取得。
	push(@MAIN_RECORD, 'sal_com_name');
	push(@MAIN_RECORD, 'sal_name');
	push(@MAIN_RECORD, 'sal_email_1');
	push(@MAIN_RECORD, 'sal_email_2');
	push(@MAIN_RECORD, 'sal_email_3');

	$dbh = &sqlwrap_db($SQLCONFIG{db_host},$SQLCONFIG{db_user},$SQLCONFIG{db_password},$SQLCONFIG{db_database});

	$IN{'send_salon_id'} = '' if($IN{'send_salon_id'} eq '');

	$sql_statement = qq| SELECT|
					.qq|    pro_id|
					.qq|   ,pro_code|
					.qq|   ,pro_name|
					.qq|   ,pro_image1|
					.qq|   ,pro_image2|
					.qq|   ,pro_image3|
					.qq|   ,(CASE WHEN agp_price_notax is null THEN pro_price_notax ELSE agp_price_notax END)  AS pro_price_notax|
					.qq|   ,(CASE WHEN agp_price is null THEN pro_price ELSE agp_price END)  AS pro_price|
					.qq|   ,pro_body|
					.qq|   ,pro_sort|
					.qq|   ,sal_com_name|
					.qq|   ,sal_name|
					.qq|   ,sal_email_1|
					.qq|   ,sal_email_2|
					.qq|   ,sal_email_3|
					.qq| FROM|
					.qq|    m_product|
					.qq| LEFT JOIN|
					.qq|    m_salon|
					.qq| ON|
					.qq|    sal_sales_id = '$IN{'send_salon_id'}'|
					.qq| LEFT JOIN|
					.qq|    m_agency_price|
					.qq| ON|
					.qq|    agp_pro_id = pro_id|
					.qq|    AND|
					.qq|    agp_age_id = sal_age_id|
					.qq| WHERE|
					.qq|    pro_valid = 10000|
					.qq| ORDER BY|
					.qq|    pro_sort|
					;

	$query = &sqlwrap_query($dbh,"$sql_statement");
	$nums = &sqlwrap_num_rows($query);
	for(my $num=0;$num < $nums;$num++) {
		$rec_val = sqlwrap_fetch_assoc($query);
		foreach $field_val (@MAIN_RECORD){
			${$field_val} = &Encode_UTF8($rec_val->{$field_val});
		}
		$item_data{"$pro_id"}{'pro_name'}	 = $pro_name;	#	商品名
		$item_data{"$pro_id"}{'pro_price'}	 = $pro_price;	#	価格
		$item_data{"$pro_id"}{'pro_body'}	 = $pro_body;	#	本文
		$item_data{"$pro_id"}{'pro_image1'}	 = $pro_image1;	#	画像

	}


	#	合計金額の初期化。
	$VAR{'totalprice'} = 0;
	$VAR{'cart_count'} = 0;

	#	注文一覧を生成する。
	for($infcnt=1; $infcnt <= $ORDER_SETLIMIT; $infcnt++){

		#	注文商品リストHTMLの初期化。
		$VAR{'admin_cart_list'} = '';
		$VAR{'user_cart_list'} = '';

		#	セッション番号を取得する。
		$VAR{'session_list_id'} = $infcnt;

		if($IN{"order_items${infcnt}"} ne ''){

			#	セッション構造化情報をカート情報と入力情報に分割する。
			@session_items = split('\|<=>\|', $IN{"order_items${infcnt}"});

			#	カート情報を取得する。
			$VAR{'subtotal'} = 0;
			@cart_items = split('\|\|', $session_items[0]);

			foreach $item (@cart_items){

				#	データが無い場合はスキップする。
				next if($item eq '');

				#	カート商品情報の取得。。
				@cart_item = split(':::', $item);
				$VAR{'pro_id'} = $cart_item[0];
				$VAR{'pro_id'} =~ s/^pro_num_(.*)/$1/;
				$VAR{'pro_num'} = $cart_item[1];
				$VAR{'pro_name'} = $item_data{"$VAR{'pro_id'}"}{'pro_name'};
				$VAR{'pro_price'} = $item_data{"$VAR{'pro_id'}"}{'pro_price'};
				$VAR{'pro_body'} = $item_data{"$VAR{'pro_id'}"}{'pro_body'};
				$VAR{'pro_image1'} = $item_data{"$VAR{'pro_id'}"}{'pro_image1'};

				#	小計算出。
				$VAR{'subtotal'} += $VAR{'pro_price'} * $VAR{'pro_num'};

				#	金額カンマ。
				$VAR{'pro_price_disp'} = $VAR{'pro_price'};
				$VAR{'pro_price_disp'} =~ s/(\d{1,3})(?=(?:\d{3})+(?!\d))/$1,/g;

				$VAR{'subtotal_disp'} = $VAR{'subtotal'};
				$VAR{'subtotal_disp'} =~ s/(\d{1,3})(?=(?:\d{3})+(?!\d))/$1,/g;

				#	商品ブロックメール生成。
				$VAR{'admin_cart_list'} .= &parse_template('contact_admin_mail_item_tr.txt');
				$VAR{'user_cart_list'} .= &parse_template('contact_user_mail_item_tr.txt');
			}

			#	注文主・送り先入力情報を取得する。
			$_cnt = 0;
			@input_items = split('::::', $session_items[1]);

			#	注文主データ取得。
			if($infcnt == 1){

				foreach $field (sort __by_inpseq keys %MAIN_REQUIRED) {

					$VAR{$field} = $input_items[$_cnt];

					#	注文2以降の送り先情報に上書きされてしまう為、ここで情報を保存する。
					$VAR{'order_'.$field} = $input_items[$_cnt];
					$_cnt++;
				}

			}

			$VAR{'cart_count'}++ if($VAR{'subtotal'} > 0);

			#	送り先ブロックメール生成。
			$VAR{'admin_item_list'} .= &parse_template('contact_admin_mail_item.txt');
			$VAR{'user_item_list'} .= &parse_template('contact_user_mail_item.txt');
			$VAR{'totalprice'} += $VAR{'subtotal'};

		}
	}

	#	注文ID。
	$VAR{'orderid'} = $$.time();

	#	連続投稿を不可とする。
	if(-e "$SETTING{'gsession_dir'}/$IN{'gsession'}.cgi"){

		#	サロン情報。
		$VAR{'sal_com_name'} = $sal_com_name;
		$VAR{'sal_name'} = $sal_name;

		#	サロン管理者メール。
		@sal_emails = ();
		push(@sal_emails, $sal_email_1) if($sal_email_1 ne '');
		push(@sal_emails, $sal_email_2) if($sal_email_2 ne '');
		push(@sal_emails, $sal_email_3) if($sal_email_3 ne '');
		$ADMIN_CC_MAIL = join(',', @sal_emails);

		#	管理者にメール送信。
		$_from = $ADMIN_SYSTEM_MAIL;
		$_mailto = $ADMIN_MAIL;
		$_mailcc = "$ADMIN_CC_MAIL";
		$_subject = qq|【VIVUS】[$VAR{'orderid'}]ご注文を受け付けました。|;
		$_messag = &parse_template("contact_admin_mail.txt");
		$_messag = &DecodeXSS($_messag);
		#	「～」、「-」の文字化けを解消する。
		$_messag =~ tr/[\x{ff5e}\x{2225}\x{ff0d}\x{ffe0}\x{ffe1}\x{ffe2}]/[\x{301c}\x{2016}\x{2212}\x{00a2}\x{00a3}\x{00ac}]/;
		$_messag = encode('SJIS', $_messag);
		$_subject = encode('SJIS', $_subject);
		&_SendMail($_from, $_mailto, $_mailcc, $_subject, $_messag);

		$_from = $ADMIN_SYSTEM_MAIL;
		$_mailto = "$VAR{'send_email'}";
		$_mailcc = '';
		$_subject = "【VIVUS】ご注文ありがとうございました。";
		$_messag = &parse_template("contact_user_mail.txt");
		$_messag = &DecodeXSS($_messag);
		#	「～」、「-」の文字化けを解消する。
		$_messag =~ tr/[\x{ff5e}\x{2225}\x{ff0d}\x{ffe0}\x{ffe1}\x{ffe2}]/[\x{301c}\x{2016}\x{2212}\x{00a2}\x{00a3}\x{00ac}]/;
		$_messag = encode('SJIS', $_messag);
		$_subject = encode('SJIS', $_subject);
		&_SendMail($_from, $_mailto, $_mailcc, $_subject, $_messag);

		# hidden保存データ破棄
		&parsedata_unlink($SETTING{'gsession_dir'}, $IN{'gsession'});

	}

	&MakeOutputHtml(\%IN, \%VAR, \$temp_file{$IN{'mode'}});

	#	正常終了。
	return $TRUE;

}



#
#	テーブル構造のオーバーライト。
#
sub		OverwriteTableStructure
{
	my($_record, $_sqlcreate) = @_;

	#	フィールド設定。(全件書換が必要)
#	@$_record = (
#		"mem_id"									,#	ID
#		"mem_add_date"								,#	登録日時
#		"mem_upd_date"								,#	更新日時
#	);

	#	データ型設定。(個々の設定が可能)
#	$$_sqlcreate{"mem_id"} = "serial";				#	ID
#	$$_sqlcreate{"mem_add_date"} = "timestamp";		#	登録日時
#	$$_sqlcreate{"mem_upd_date"} = "timestamp";		#	更新日時

	#	正常終了。
	return $TRUE;

}


#
#	入力値コンバート
#
sub		item_conv
{
	my($mode) = @_;

	&ConvertDataDisplayForm(\%MAIN_REQUIRED, \%MAIN_CHECKED, \%VAR, \$mode);

}

#
#	入力内容確認
#
sub		item_check
{

	my($mode) = @_;

	my(@suffixlist);
	my($suffix);

	$ret = &input_check(\%MAIN_REQUIRED, \%MAIN_CHECKED, \%IN, $mode);

	#	確認メールアドレスの入力値を確認する。
	if($IN{'send_email'} ne $IN{'send_email_check'}){
		$ret = $TRUE;
		$VAR{'send_email_check_err'} = 'メールアドレスと異なります。';
	}

	#	商品選択の確認。
	my($item_num);

	$dbh = &sqlwrap_db($SQLCONFIG{db_host},$SQLCONFIG{db_user},$SQLCONFIG{db_password},$SQLCONFIG{db_database});

	$VAR{'sal_age_id'} = null if($VAR{'sal_age_id'} eq '');

	$sql_statement = qq| SELECT|
					.qq|    * |
					.qq| FROM|
					.qq|    m_product|
					.qq| LEFT JOIN|
					.qq|    m_agency_price|
					.qq| ON|
					.qq|    agp_age_id = $VAR{'sal_age_id'}|
					.qq| ORDER BY|
					.qq|    pro_sort|
					;
	$query = &sqlwrap_query($dbh,"$sql_statement");
	$nums = &sqlwrap_num_rows($query);

	$item_num = 0;
	for(my $num=0;$num < $nums;$num++) {
		$rec_val = sqlwrap_fetch_assoc($query);
		$VAR{'pro_id'} = $rec_val->{'pro_id'};
		$item_num += $IN{"pro_num_$VAR{'pro_id'}"};
	}
	if($item_num <= 0){
		$ret = $TRUE;
		$VAR{'pro_num_err'} = '商品を選択してください。';
	}

	return($ret);

}

#
#	検索条件を設定する。
#
sub		MakeSQLwherevalue
{
	my($_item_, $_wherewords_) = @_;
	my(@wherewords);
	my($whereword);
	my($search_key_mem_name);

	$$_wherewords_ = '';

	foreach $s_val(keys %LIST_SERACH){

		#	LIKE検索。
		if($LIST_SERACH{"$s_val"}[0] eq 'LIKE'){

			#	外部入力文字列のエンコード。
			$$_item_{"$s_val"}		= &EncodeXSS($$_item_{"$s_val"});

			push(@wherewords, qq/${s_val} LIKE '%$$_item_{"s_${s_val}"}%'/) if($$_item_{"s_${s_val}"} ne '');


		#	日付範囲検索。
		}elsif($LIST_SERACH{"$s_val"}[0] eq 'DATE'){

			#	外部入力文字列のエンコード。
			$$_item_{"${s_val}_s"}		= &EncodeXSS($$_item_{"${s_val}_s"});
			$$_item_{"${s_val}_e"}		= &EncodeXSS($$_item_{"${s_val}_e"});

			$$_item_{"s_${s_val}_s"} =~ s|/|-|g;
			$$_item_{"s_${s_val}_e"} =~ s|/|-|g;
			push(@wherewords, qq/${s_val} >= '$$_item_{"s_${s_val}_s"} 00:00:00'/) if($$_item_{"s_${s_val}_s"} ne '');
			push(@wherewords, qq/${s_val} <= '$$_item_{"s_${s_val}_e"} 23:59:59'/) if($$_item_{"s_${s_val}_e"} ne '');

		#	その他指定検索。
		}else{

			#	外部入力文字列のエンコード。
			$$_item_{"$s_val"}		= &EncodeXSS($$_item_{"$s_val"});

			#	指定検索の値を設定する。
			$$_item_{"s_${s_val}"} = $LIST_SERACH{"$s_val"}[2] if($LIST_SERACH{"$s_val"}[2] ne '');

			if($LIST_SERACH{"$s_val"}[1] eq 'int'){

				push(@wherewords, qq/${s_val} $LIST_SERACH{"$s_val"}[0] $$_item_{"s_${s_val}"}/) if($$_item_{"s_${s_val}"} ne '');

			}else{

				push(@wherewords, qq/${s_val} $LIST_SERACH{"$s_val"}[0] '$$_item_{"s_${s_val}"}'/) if($$_item_{"s_${s_val}"} ne '');

			}

		}

	}

	#	その他の検索。
	#	SAMPLE
	#$$_item_{'name'}		= &EncodeXSS($$_item_{'name'});
	#push(@wherewords, "name LIKE '%$$_item_{s_name}%'") if($$_item_{s_name} ne '');
	#	SAMPLE

	$whereword = join(' AND ', @wherewords);
	if($whereword) {
		$$_wherewords_ = " WHERE ${whereword}";
	}

	#	正常終了。
	return $TRUE;

}


#
#	教室予約設定処理。
#
sub		SyncscPrice
{
	my($dbh);
	my(@RESERVE_RECORD);
	my(%notsqlcreate);
	my($sqlitem);
	my($record);
	my($sql_statement);
	my($query);
	my(@agp_price);
	my(@agp_price_notax);

	$IN{'sal_id'} = '' if($IN{'sal_id'} eq '');

	$dbh = &sqlwrap_db($SQLCONFIG{db_host},$SQLCONFIG{db_user},$SQLCONFIG{db_password},$SQLCONFIG{db_database});

	#	入力されたパートナーIDの確認。
	$sql_statement = qq| SELECT|
					.qq|    * |
					.qq| FROM|
					.qq|    m_salon|
					.qq| WHERE|
					.qq|    sal_sales_id = '$IN{'sal_id'}'|
					;

	$query = &sqlwrap_query($dbh,"$sql_statement $limit_str");
	$nums = &sqlwrap_num_rows($query);

	if($nums <= 0){

		#	パートナーIDの存在が無い場合エラー。
		if($IN{'sal_id'} ne ''){
			$VAR{'StatusAlert'} = '指定のパートナーIDに誤りがあります。';
		}

		#	基本価格に戻す。
		$sql_statement = qq| SELECT|
						.qq|    * |
						.qq| FROM|
						.qq|    m_product|
						.qq| ORDER BY|
						.qq|    pro_sort|
						;
		$query = &sqlwrap_query($dbh,"$sql_statement");
		$nums = &sqlwrap_num_rows($query);
		for(my $num=0;$num < $nums;$num++) {
			$rec_val = &sqlwrap_fetch_assoc($query);
			push(@agp_price_notax, $rec_val->{'pro_price_notax'});
			push(@agp_price, $rec_val->{'pro_price'});
		}

	}else{

		#	代理店ID取得。
		$rec_val = &sqlwrap_fetch_assoc($query);
		$VAR{'sal_age_id'} = &Encode_UTF8($rec_val->{'sal_age_id'});
		$VAR{'sal_com_name'} = &Encode_UTF8($rec_val->{'sal_com_name'});

		$VAR{'sal_age_id'} = null if($VAR{'sal_age_id'} eq '');

		#	代理店別の商品価格を取得する。
		$sql_statement = qq| SELECT|
						.qq|    * |
						.qq| FROM|
						.qq|    m_product|
						.qq| LEFT JOIN|
						.qq|    m_agency_price|
						.qq| ON|
						.qq|    agp_age_id = $VAR{'sal_age_id'}|
						.qq| ORDER BY|
						.qq|    pro_sort|
						;
		$query = &sqlwrap_query($dbh,"$sql_statement");
		$nums = &sqlwrap_num_rows($query);
		for(my $num=0;$num < $nums;$num++) {
			$rec_val = &sqlwrap_fetch_assoc($query);
			push(@agp_price_notax, $rec_val->{'agp_price_notax'});
			push(@agp_price, $rec_val->{'agp_price'});
		}

	}

	$VAR{'price_notax_list'} = join(',', @agp_price_notax);
	$VAR{'price_list'} = join(',', @agp_price);

	my(%returnhtmldata);
	print "Content-type: text/html;\n\n";

	$returnhtmldata = {
		 'StatusCode' => "ok"
		,'ResAsyncError' => "$VAR{'ResAsyncError'}"
		,'StatusAlert' => "$VAR{'StatusAlert'}"
		,'ResAsyncSalonComName' => "$VAR{'sal_com_name'}"
		,'ResAsyncPriceNotaxList' => "$VAR{'price_notax_list'}"
		,'ResAsyncPriceList' => "$VAR{'price_list'}"
		,'DEBUG' => "$VAR{'DEBUG'}"
	};
	$return_res_json = encode_json($returnhtmldata);
	print $return_res_json;
	exit;

}

