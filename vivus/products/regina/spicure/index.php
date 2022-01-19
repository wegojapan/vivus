<!doctype html>
<html>
<head>
<?php include "../../../inc/meta.php"; ?>

     
<title>Vivus regina SPI:CURE</title>
    
<!-- CSS Link --> 
<link rel="stylesheet" href="../../../css/product.css"/>
    
<!-- JS Link -->    
    
    
<?php include "../../../inc/config.php"; ?>
<?php include "../../../inc/head.php"; ?>    
<?php include "../../../inc/include_slick.php"; ?>
    
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
    <?php include_once('../../../inc/header.php'); ?>
    <div id="con_page" class="page_product">
        <section class="con_product">
            <div class="con_tit">
                <h2 class="st">
                    <small>VIVUS REGINA</small>
                    <strong>SPI:CURE SERIES</strong>
                </h2>
                <p class="txt">天然スピキュールのチカラで<br>内側からもっと美しく</p>
                <dl class="box_nav en view_pc-tab">
                    <dt>COLLECTION</dt>
                    <dd class="active">SPI:CURE SERIES</dd>
                </dl>
            </div>
            <div class="con_item no2">
                <ul class="box_item">
                    <li class="item"><a href="./7ampoule.php">
                        <div class="img"><img src="./imgs/thum_item_7am.jpg" alt=""></div>
                        <dl class="box_txt">
                            <dt class="st">
                                <strong>7AMPOULES SHINING</strong>
                                <span>7アンプルズシャイニング</span>
                            </dt>
                            <dd class="txt">透明感のあるクリアな素肌へ導くデイリーアンプル</dd>
                        </dl>
                    </a></li>
                    <li class="item"><a href="./aquacream.php">
                        <div class="img"><img src="./imgs/thum_item_aqua.jpg" alt=""></div>
                        <dl class="box_txt">
                            <dt class="st">
                                <strong>AQUA CREAM</strong>
                                <span>アクアクリーム</span>
                            </dt>
                            <dd class="txt">健康なお肌のためのブライトニング水分クリーム</dd>
                        </dl>
                    </a></li>
                    <li class="item"><a href="./cleansing.php">
                        <div class="img"><img src="./imgs/thum_item_foam.jpg" alt=""></div>
                        <dl class="box_txt">
                            <dt class="st">
                                <strong>CLEANSING FOAM</strong>
                                <span>クレンジングフォーム</span>
                            </dt>
                            <dd class="txt">つっぱらずしっとりとした角質ケア洗顔フォーム</dd>
                        </dl>
                    </a></li>
                </ul>
            </div>
        
        </section>
        
    </div>
    <?php include_once('../../../inc/footer.php'); ?>

    
</body>
</html>














