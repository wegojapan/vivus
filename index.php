<!doctype html>
<html>
<head>
<?php include("./inc/gtag.php");?>    
<?php include("./inc/meta.php");?>    


     
<title>WEGO JAPAN</title>
<?php include("./inc/config.php");?>    
<?php include("./inc/head.php");?>    
<?php include("./inc/include_slick.php");?>    

    
    
<!-- CSS Link --> 
<link rel="stylesheet" href="../css/main.css"/>
    
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
            autoplaySpeed: 4000,
            fade: true
        });
        $('.box_list').slick({
            dots: true,
            slidesToShow: 4,
            slidesToScroll: 4,
            responsive: [
                {
                  breakpoint: 1025,
                  settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                  }
                },
                {
                  breakpoint: 769,
                  settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                  }
                },
                {
                  breakpoint: 480,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                  }
                } 
            ]
        });
        
        $('.box_slider_vision').slick({
            centerMode: true,
            centerPadding: '45px',
            slidersToShow: 3,
            variableWidth: true
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
            </div>
            <div class="con_slogan">
                <div class="box_slogan">
                    <span>新しい価値を創造して世界をつなぐ</span>
                    <strong class="en">WE WILL GO TOGETHER</strong>
                    <em>変化の中心、共存を通して、<br class="view_sp">新しい未来を作っていきます。</em>
                    <small class="en">WEGO JAPAN INTERNATIONAL</small>
                </div>
            </div>
            <ul class="box_sns view_pc">
                <li><a href="https://www.instagram.com/wego_jp/" target="_blank"><i class="fab fa-instagram"></i></a></li>
                <li><a href="#123"><i class="fab fa-youtube"></i></a></li>
                <li><a href="#123"><i class="fab fa-facebook-f"></i></a></li>
            </ul>
        </section>
        
        <section class="con_story">
            <h2 class="tit">
                <strong class="en">OUR STORY</strong>
                <small>様々なお知らせを確認してください。</small>
            </h2>
            <article class="box_story">
                <div class="box_list">
                    <div class="card"><a href="./story/view_post_regina.php">
                        <p class="img"><img src="../imgs/img_thum_regina.jpg" alt=""></p>
                        <dl>
                            <dt>ビーバースレジーナエスピーアイ：キュアシリーズ</dt>
                            <dd>きれいで細かく洗練されたナノスピキュールのみを使用したホームケアデイリー製品です。</dd>
                        </dl>
                    </a></div>
                    <div class="card"><a href="./story/view_post_stk.php">
                        <p class="img"><img src="../imgs/img_thum_sun.jpg" alt=""></p>
                        <dl>
                            <dt>日焼け止めを塗るタイミングを知らせるUV遮断通知ステッカー！</dt>
                            <dd>アメリカの特許を受けた日焼け止めを塗るタイミングを知らせる紫回線遮断通知ステッカー</dd>
                        </dl>
                    </a></div>
                    <div class="card"><a href="./story/view_post_patch.php">
                        <p class="img"><img src="../imgs/img_thum_patch.jpg" alt=""></p>
                        <dl>
                            <dt>ゴルフを愛するあなた！もう日焼け止めだけでは足りない！</dt>
                            <dd>両面ファブリック UVカット特殊生地を使用、肌保湿、老化防止、肌の再生力を改善したパッチ[特許出願]</dd>
                        </dl>
                    </a></div>
                    <div class="card"><a href="./story/view_post_cooling.php">
                        <p class="img"><img src="../imgs/img_thum_cooling.jpg" alt=""></p>
                        <dl>
                            <dt>皮膚の温度下げるウィゴークーリング</dt>
                            <dd>朝、浮腫んだ顔と目の腫れを抑えるときに使用したり、熱がこもった肌の鎮静にぴったりのクーリングスティックです。</dd>
                        </dl>
                    </a></div>
                    <div class="card"><a href="./story/view_post_mask.php">
                        <p class="img"><img src="../imgs/img_thum_mask.jpg" alt=""></p>
                        <dl>
                            <dt>銅マスクで抗菌・消臭！ マスクストラップで忘れ物防止！</dt>
                            <dd>コロナ時代に弊社の銅マスクを使用することにより、健康管理に役立ち、地球環境を守ることができます。</dd>
                        </dl>
                    </a></div>
                </div>
            </article>
        </section>
        
        <section class="con_vision">
            <div class="box_top">
                <h2 class="tit en">
                    <small>OUR VISION</small>
                    <strong class="en">WE CONNECT<br>WITH THE WORLD</strong>
                </h2>
                <dl class="txt">
                    <dt>人と人をつなぐ企業,<br>持続可能な 成長を通じて<br class="view_sp">より良い未来を作っていきます。</dt>
                    <dd>私達は コアバリューの実践を通じて信頼される企業を超え<br class="view_tab">世界的に愛されるグローバル 企業へと成長するため、努力しています</dd>
                </dl>
            </div>
            <ul class="box_slider_vision">
                <li><img src="./imgs/img_inte_01.jpg" alt=""></li>
                <li><img src="./imgs/img_inte_02.jpg" alt=""></li>
                <li><img src="./imgs/img_inte_03.jpg" alt=""></li>
                <li><img src="./imgs/img_inte_01.jpg" alt=""></li>
                <li><img src="./imgs/img_inte_02.jpg" alt=""></li>
                <li><img src="./imgs/img_inte_03.jpg" alt=""></li>
            </ul>
            <p class="btn_more"><a href="./company/">詳しくはこちらへ</a></p>
        </section>
        
        <section class="con_biz">
            <h2 class="tit en">
                <small class="en">WHAT WE DO</small>
                <strong class="en">BUSINESS</strong>
            </h2>
            <article class="box_biz">
                <div class="biz_card"><a href="./business/#oem">
                    <p class="img"><img src="./imgs/img_cate_01.jpg" alt=""></p>
                    <dl>
                        <dt>
                            <strong class="en">MANUFACTURING</strong>
                            <small>OEM 制作 / 輸入 / 納品</small>
                        </dt>
                        <dd>商品のOEM制作、ご相談はもちろん、 <br class="view_pc-tab">デザインから製品発売までの全過程をサポートします。</dd>
                    </dl>
                </a></div>
                <div class="biz_card"><a href="./business/#food">
                    <p class="img"><img src="./imgs/img_cate_02.jpg" alt=""></p>
                    <dl>
                        <dt>
                            <strong class="en">FRANCHISE</strong>
                            <small>外食&amp;フランチャイズ</small>
                        </dt>
                        <dd>自分の店が欲しいなら！ <br class="view_pc-tab">インテリアからオープンまで全方向に対応しています。</dd>
                    </dl>
                </a></div>
                <div class="biz_card"><a href="./business/#ebiz">
                    <p class="img"><img src="./imgs/img_cate_03.jpg" alt=""></p>
                    <dl>
                        <dt>
                            <strong class="en">e - BUSINESS</strong>
                            <small>インターネットビジネス</small>
                        </dt>
                        <dd>専門的な知識がなくてもオンラインビジネスを運営できるよう支援しています。</dd>
                    </dl>
                </a></div>
                <div class="biz_card"><a href="./business/#consulting">
                    <p class="img"><img src="./imgs/img_cate_04.jpg" alt=""></p>
                    <dl>
                        <dt>
                            <strong class="en">CONSULTING</strong>
                            <small>コンサルティング</small>
                        </dt>
                        <dd>私たちはクライアントの成功的な成長のために様々な分野の専門家による相談を支援しています。</dd>
                    </dl>
                </a></div>
            </article>
            <p class="btn_more"><a href="./business">詳しくはこちらへ</a></p>
        </section>
        
        <section class="con_md_slogan view_pc">
            <div class="box_md_slogan">
                <div class="box_slogan">
                    <span>新しい価値を創造して世界をつなぐ</span>
                    <strong class="en">WE WILL GO TOGETHER</strong>
                    <em>変化の中心、共存を通して、新しい未来を作っていきます。</em>
                    <small class="en">WEGO JAPAN INTERNATIONAL</small>
                </div>
            </div>
        </section>
        
        <section class="con_contact">
            <div class="box_contact">
                <p class="txt">顧客との信頼をもとに <br class="view_sp">成功的な関係を築いていきます。<br>ウィゴージャパンとともに新たなスタートを</p>
                <p class="btn_more"><a href="./contact/">お問い合わせ</a></p>
            </div>
        </section>
        
    </div>
    <?php include('./inc/footer.php'); ?>

    
</body>
</html>














