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
        <div class="con_int apply thanks">
            <h2 class="tit">
                <span class="tit_en">VIVUS PARTNER</span>
                <small class="txt">パートナー申請フォーム</small>
            </h2>
        </div>
        <div class="con_cont apply">
            <div class="box_thanks">
                <h1>ありがとうございます。</h1>
                <p class="txt">
                    入力した内容が送信されました。<br>
                    内容を確認した後、担当者から<br class=view_sp>ご連絡いたします。
                </p>
                <p class="btn_ok">
                    <a href="../">TOPに戻る</a>
                </p>
            </div>
        </div>
    </div>
    <?php include_once('../inc/footer.php'); ?>

    
</body>
</html>














