<!doctype html>
<html>
<head>
<?php include("./inc/meta.php");?>    


     
<title>VIVUS</title>
<?php include("./inc/config.php");?>    
<?php include("./inc/head.php");?>    
<?php include("./inc/include_slick.php");?>    

    
    
<!-- CSS Link --> 
<link rel="stylesheet" href="../vivus/css/main.css"/>
    
<!-- data-aos="fade-up" data-aos-delay="0" -->
    
    
<!-- JS Link -->    
    
<script language="javascript">
    $(function(){
        $('.box_slider').slick({
            dots: false,
            arrows: false,
            customPaging : function(slider, i) {
                var thumb = $(slider.$slides[i]).data();
                return '<a>'+('0'+(i+1)).slice(-2)+'</a>';
                        },
            autoplay: true,
            autoplaySpeed: 5000,
            fade: true
        });        
        $('.btn_menu').on('click',function(e){
            $(this).toggleClass('active');
            $('.open_menu').toggleClass('active');
        });
    })
</script>
</head>

    
<body>
    
    <?php include('./inc/header.php'); ?>
    <div id="con_page">
        <section class="con_main">
            <div class="box_slider">
                <div class="slider_01"></div>
                <div class="slider_02"></div>
            </div>
            <div class="con_slogan">
                <div class="box_slogan" data-aos="fade-up" data-aos-delay="0">
                    <p class="logo"><img src="./imgs/common/bi_vivus.svg" alt=""></p>
                    <p class="slogan">LOVE YOUR SKIN<br>IN YOUR LIFE</p>
                </div>
            </div>
            <ul class="box_sns view_pc">
                <li><a href="https://www.instagram.com/wego_jp/" target="_blank"><i class="fab fa-instagram"></i></a></li>
                <li><a href="#123"><i class="fab fa-youtube"></i></a></li>
                <li><a href="#123"><i class="fab fa-facebook-f"></i></a></li>
            </ul>
        </section>
        
        <section class="con_int">
            <h2 class="tit" data-aos="fade-up" data-aos-delay="0">開発者自身が<br>心から使いたいと思う<br>商品をめざして。</h2>
            <p class="txt" data-aos="fade-up" data-aos-delay="0">
                長年の韓国式エステの経験を生かして、自分たちが心から使いたいと思う商品だけをリリースする「VIVUS」。<br class="view_pc">サロンでのお手入れの効果を高める働きが期待できるため、お客様にも自信を持ってご紹介いただけます。
            </p>
            <p class="btn_more">
                <a href="">MORE</a>
            </p>
        </section>
        
        <section class="con_cate cate_regina">
            <div class="box_cate">
                <div class="box_item">
                    <p class="item" data-aos="fade-up" data-aos-delay="0"><img src="./imgs/item_cream.png" alt=""></p>
                    <p class="logo" data-aos="fade-up" data-aos-delay="0"><img src="./imgs/common/bi_regina.svg" alt=""></p>
                </div>
                <div class="box_txt">
                    <h3 class="tit" data-aos="fade-up" data-aos-delay="0">天然スピキュールのチカラで<br>内側からもっと美しく</h3>
                    <p class="txt" data-aos="fade-up" data-aos-delay="0">
                        Vivus regina（ビーバースレジーナ）は、「上質なスキンケアアイテムを、デイリーケアに」をコンセプトに作られたブランドです。<br class="view_pc">天然由来の成分にこだわって作られたスキンケアアイテムは、疲れた肌をそっとフォロー。肌の乾燥や、かさつきが気になる人にしっかりと寄り添い、いつまでも透明感のある美しい肌作りをお手伝いしています。
                    </p>
                    <p class="btn_more">
                        <a href="./products/regina/spicure/">MORE</a>
                    </p>
                </div>            
            </div>
        </section>
        
        <section class="con_cate cate_golf">
            <div class="box_cate">
                <div class="box_item">
                    <p class="item" data-aos="fade-up" data-aos-delay="0"><img src="./imgs/item_golf.png" alt=""></p>
                    <p class="logo" data-aos="fade-up" data-aos-delay="0"><img src="./imgs/common/bi_golf.svg" alt=""></p>
                </div>
                <div class="box_txt">
                    <h3 class="tit" data-aos="fade-up" data-aos-delay="0">紫外線から素肌を守る<br>ラウンド中の専用ケア</h3>
                    <p class="txt" data-aos="fade-up" data-aos-delay="0">
                        ゴルフラウンド中の肌の損傷に対する心配はもう終わり。<br class="view_pc">ゴルフが大好きでコスメについて最も詳しいブランド、VIVUSからゴルフ専用コスメブランド、VIVUSゴルフが誕生しました。<br class="view_pc">これからは、VIVUSゴルフの様々な製品でラウンド中にあなたの肌をケアしてみてください。
                    </p>
                    <p class="btn_more">
                        <a href="">MORE</a>
                    </p>
                </div>            
            </div>
        </section>
        
        <section class="con_util">
            <dl class="box_util util_faq"><a href="#123">
                <dt class="tit_en">FAQ</dt>
                <dd>よくあるご質問</dd>
            </a></dl>
            <dl class="box_util util_shop"><a href="#123">
                <dt class="tit_en">SHOP LIST</dt>
                <dd>ショップの一覧</dd>
            </a></dl>
        </section>
        
        
    </div>
    <?php include('./inc/footer.php'); ?>

    
</body>
</html>














