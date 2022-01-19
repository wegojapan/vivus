<!doctype html>
<html>
<head>
<?php include "../inc/meta.php"; ?>

     
<title>VIVUS PRODUCT</title>
    
<!-- CSS Link --> 
<link rel="stylesheet" href="../css/product.css"/>
    
<!-- JS Link -->    
    
    
<?php include "../inc/config.php"; ?>
<?php include "../inc/head.php"; ?>    
<?php include "../inc/include_slick.php"; ?>
    
<script language="javascript">
    $(function(){
        $('.btn_menu').on('click',function(e){
            $(this).toggleClass('active');
            $('.open_menu').toggleClass('active');
        });
    })
</script>
</head>

    
<body>
    <?php include_once('../inc/header.php'); ?>
    <div id="con_page">
        <section class="con_regina">
            <div class="box_intro">
                <h2 class="logo"><img src="../imgs/common/bi_regina.svg" alt=""></h2>
                <dl class="box_txt">
                    <dt>LOVE YOUR SKIN IN YOUR LIFE</dt>
                    <dd>上質なスキンケアアイテムを、デイリーケアに</dd>
                </dl>
            </div>
            <div class="box_spi">
                <div class="box_img"></div>
                <div class="box_txt">
                    <div class="tit">
                        <small>VIVUS REGINA</small>
                        <h3>SPI:CURE SERIES</h3>
                    </div>
                    <p class="txt">
                        レジーナスピキュールシリーズは純度の高い海から採れたスピキュールを使用しています。微細な針が肌に効果的な成分を奥深くまで浸透させ、透明感のある健康的な肌へ導きます。
                    </p>
                    <p class="btn_more"><a href="#123">MORE</a></p>
                </div>
            </div>
        </section>
        
    </div>
    <?php include_once('../inc/footer.php'); ?>

    
</body>
</html>














