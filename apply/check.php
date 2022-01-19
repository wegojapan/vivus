<!doctype html>
<html>
<head>
<?php include "../inc/gtag.php"; ?>    
<?php include "../inc/meta.php"; ?>

     
<title>パートナー申込</title>
    
<!-- CSS Link --> 
<link rel="stylesheet" href="../css/form.css"/>
        
<?php include "../inc/config.php"; ?>
<?php include "../inc/head.php"; ?>    
<?php include "../inc/include_slick.php"; ?>
    
<!-- JS Link -->    
<script type="text/javascript" src="../../js/jquery.autoKana.js"></script>   
    
<script language="javascript">
    $(function(){
        $.fn.autoKana('input[name="store"] ', 'input[name="skana"]', {katakana:true});
        $.fn.autoKana('input[name="name"] ', 'input[name="kana"]', {katakana:true});
        $('.btn_menu').on('click',function(e){
            $(this).toggleClass('active');
            $('.open_menu').toggleClass('active');
            $('.box_header .logo').toggleClass('active');
        });
        $('.box_item label').on('click',function(e){
            $(this).toggleClass('active');
        });
    })
</script>
</head>

    
<body>
    <?php include_once('../inc/header.php'); ?>
    <div id="con_page">
        <div class="con_int apply">
            <p class="tit" data-aos="fade-up" data-aos-delay="0">Vivusパートナーを考える<br class="view_sp">サロン様に<br>ご希望のサロン様は以下の様式に情報を<br class="view_sp">入力してください。</p>
        </div>
        <div class="con_cont apply">
            <article class="box_cont">
                <h2 class="tit">
                    <span>APPLY</span>
                    <small class="txt">パートナー申込</small>
                </h2>
                <p class="st">入力項目はすべて必須項目になります</p>
                <form>
                    <fieldset class="form_info">
                        <p class="form_double">
                            <label for="store error">店名</label>
                            <input type="text" name="store" id="store"　placeholder="店名を入力してください。" required>
                            <input type="text" name="skana" id="store2" placeholder="フリガナ" required>
                        </p>
                        <p class="form_double">
                            <label for="name">ご担当者様氏名</label>
                            <input type="text" name="name" id="name"　placeholder="お名前を入力してください。" required>
                            <input type="text" name="kana" id="name2" placeholder="フリガナ" required>
                        </p>
                        <p>
                            <label>営業担当者</label>
                            <select name="Seller" id="Seller">
                                <option value="">担当営業なし</option>
                                <option value="">営業担当者_01</option>
                                <option value="">営業担当者_02</option>
                            </select>
                        </p>
                        <p>
                            <label for="tel">電話番号</label>
                            <input type="tel" name="tel" id="tel" required>
                        </p>
                        <p>
                            <label for="mail">メールアドレス</label>
                            <input type="email" name="mail" id="mail" required>
                        </p>
                        <div class="box_choice">
                            <label>取扱希望商品</label>
                            <small class="txt">取扱をご希望の商品を全てチェックしてください。</small>
                            <ul class="box_item">
                                <li class="item active">
                                    <label class="en" for="amp"><img src="../../products/regina/spicure/imgs/thum_item_7am.png" alt="">7AMPOULES</label>
                                    <input type="checkbox" id="amp" name="amp" value="amp">
                                </li>
                                <li class="item">
                                    <label class="en" for="aqua"><img src="../../products/regina/spicure/imgs/thum_item_aqua.png" alt="">AQUA CREAM</label>
                                    <input type="checkbox" id="aqua" name="aqua" value="aqua">
                                </li>
                                <li class="item">
                                    <label class="en" for="foam"><img src="../../products/regina/spicure/imgs/thum_item_foam2.png" alt="">Cleansing Foam</label>
                                    <input type="checkbox" id="foam" name="foam" value="foam">
                                </li>
                                <li class="item">
                                    <label class="en" for="vsera"><img src="../../products/regina/spicure/imgs/thum_item_vsera.png" alt="">CICA V.SERA</label>
                                    <input type="checkbox" id="vsera" name="vsera" value="vsera">
                                </li>
                                <li class="item">
                                    <label class="en" for="toner"><img src="../../products/regina/spicure/imgs/thum_item_attirance.png" alt="">Attirance Toner</label>
                                    <input type="checkbox" id="toner" name="toner" value="toner">
                                </li>
                            </ul>
                        </div>
                        <p>
                            <label for="msg">その他お問い合わせ内容</label>
                            <textarea name="msg" id="msg" cols="30" rows="5"></textarea>
                        </p>
                    </fieldset>
                    <div class="box_law">
                        <dl class="box_top">
                            <dt>個人情報の取り扱いについて</dt>
                            <dd>弊社では、個人情報を厳重に管理するために、<br class="view_sp">以下の内容を実施します。</dd>
                        </dl>
                        <div class="box_txt">
                            <p class="txt">
                                個人情報は、弊社の個人情報保護マニュアルや内部規程に従って適正に管理します。<br>
                                個人情報は、相談者の同意なく第三者に提供されず、以下の目的でのみ使用されます。
                            </p>
                            <ul>
                                <li>
                                    <h3>収集する個人情報項目</h3>
                                    <dl>
                                        <dt>収集項目</dt>
                                        <dd>お名前、メールアドレス、電話番号など</dd>
                                    </dl>
                                    <dl>
                                        <dt>収集方法</dt>
                                        <dd>ホームページ 入力フォーム</dd>
                                    </dl>
                                </li>
                                <li>
                                    <h3>個人情報の収集及び利用目的</h3>
                                    <p>相談のお問い合わせ、自社広報マーケティングなどに活用</p>
                                </li>
                            </ul>
                        </div>
                        <p class="box_agree">
                            <input type="checkbox" id="check" required>
                            <label for="check">個人情報の取り扱いについて同意する</label>
                        </p>
                    </div>
                    <p class="btn_send">
                        <input type="submit" value="パートナー申込する">
                    </p>
                </form>            
            </article>
        </div>
        
        
    </div>
    <?php include_once('../inc/footer.php'); ?>

    
</body>
</html>














