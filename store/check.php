<!doctype html>
<html>
<head>
<?php include "../inc/gtag.php"; ?>    
<?php include "../inc/meta.php"; ?>

     
<title>パートナー申込確認</title>
    
<!-- CSS Link --> 
<link rel="stylesheet" href="../css/form.css"/>
        
<?php include "../inc/config.php"; ?>
<?php include "../inc/head.php"; ?>    
<?php include "../inc/include_slick.php"; ?>
    
<!-- JS Link -->    
<script type="text/javascript" src="../../js/jquery.autoKana.js"></script>   
    
<script language="javascript">
    $(function(){
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
        <div class="con_cont apply check">
            <article class="box_cont">
                <h2 class="tit">
                    <span>APPLY CHECK</span>
                    <small class="txt">パートナー申請フォーム確認</small>
                </h2>
                <div class="box_check">
                    <dl>
                        <dt class="shop">店名</dt>
                        <dd>
                            <span>店名</span>
                            <span>ミセメイ</span>
                        </dd>
                        
                        <dt class="name">ご担当者様氏名</dt>
                        <dd>
                            <span>担当者</span>
                            <span>タントウシャ</span>
                        </dd>
                        
                        <dt class="sales">営業担当者</dt>
                        <dd>営業担当者_01</dd>
                        
                        <dt class="tel">電話番号</dt>
                        <dd>00000000000</dd>
                        
                        <dt class="mail">メールアドレス</dt>
                        <dd>mail@gmail.com</dd>
                        
                        <dt class="msg">取扱希望商品</dt>
                        <dd>
                            <ul class="box_list">
                                <li>7AMPOULES</li>
                                <li>AQUA CREAM</li>
                            </ul>
                        
                        </dd>
                        
                        <dt>その他お問い合わせ内容</dt>
                        <dd>テキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキストテキスト</dd>
                    </dl>
                    <div class="box_btn">
                        <p class="btn btn_prev"><a href="./">また修正する</a></p>
                        <p class="btn btn_ok"><a href="./thanks.php">パートナー申込する</a></p>
                    </div>
                </div>
            </article>
        </div>
        
        
    </div>
    <?php include_once('../inc/footer.php'); ?>

    
</body>
</html>














