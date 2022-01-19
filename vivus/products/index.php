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
        <section class="wrp_product">
            <div class="con_intro regina">
                <div class="box_intro" data-aos="fade-up" data-aos-delay="500">
                    <h2 class="logo" data-aos="fade-up" data-aos-delay="0"><img src="../imgs/common/bi_regina.svg" alt=""></h2>
                    <dl class="box_txt">
                        <dt class="tit_en">LOVE YOUR SKIN <br class="view_tab-sp">IN YOUR LIFE</dt>
                        <dd class="txt">上質なスキンケアアイテムを、デイリーケアに</dd>
                    </dl>
                </div>
            </div>
            <article class="con_series con_spi">
                <div class="box_img" data-aos="fade-left" data-aos-delay="100"></div>
                <div class="box_txt" data-aos="fade-up" data-aos-delay="500">
                    <div class="st">
                        <small>VIVUS REGINA</small>
                        <h3>SPI:CURE SERIES</h3>
                    </div>
                    <p class="txt">
                        レジーナスピキュールシリーズは純度の高い海から採れたスピキュールを使用しています。微細な針が肌に効果的な成分を奥深くまで浸透させ、透明感のある健康的な肌へ導きます。
                    </p>
                    <p class="btn_more"><a href="./regina/spicure/">MORE</a></p>
                </div>
            </article>
            <div class="con_intro golf">
                <div class="box_intro" data-aos="fade-up" data-aos-delay="500">
                    <h2 class="logo" data-aos="fade-up" data-aos-delay="0"><img src="../imgs/common/bi_golf.svg" alt=""></h2>
                    <dl class="box_txt" data-aos="fade-up" data-aos-delay="0">
                        <dt class="tit_en">CARE YOUR SKIN <br class="view_tab-sp">ON FAIRWAY</dt>
                        <dd class="txt">ゴルフが大好きでコスメについて最も詳しいブランド</dd>
                    </dl>
                </div>
            </div>
            <article class="con_series con_golf">
                <div class="box_img" data-aos="fade-right" data-aos-delay="100"></div>
                <div class="box_txt" data-aos="fade-up" data-aos-delay="500">
                    <div class="st">
                        <h3>VIVUS GOLF SERIES</h3>
                    </div>
                    <p class="txt">
                        レジーナスピキュールシリーズは純度の高い海から採れたスピキュールを使用しています。微細な針が肌に効果的な成分を奥深くまで浸透させ、透明感のある健康的な肌へ導きます。
                    </p>
                    <p class="btn_more"><a href="#123">MORE</a></p>
                </div>
            </article>
        </section>
        
    </div>
    <?php include_once('../inc/footer.php'); ?>

    
</body>
</html>














