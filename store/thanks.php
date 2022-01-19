<!doctype html>
<html>
<head>
<?php include "../inc/gtag.php"; ?>    
<?php include "../inc/meta.php"; ?>

     
<title>Partner's Mall</title>
    
<!-- CSS Link --> 
<link rel="stylesheet" href="../css/form.css"/>
    
<?php include "../inc/config.php"; ?>
<?php include "../inc/head.php"; ?>    
<?php include "../inc/include_slick.php"; ?>
    
<!-- JS Link -->    
<script type="text/javascript" src="../../js/jquery.autoKana.js"></script>   
    
<script language="javascript">
    $(function(){
        $.fn.autoKana('input[name="name"] ', 'input[name="kana"]', {katakana:true});
        $('.btn_menu').on('click',function(e){
            $(this).toggleClass('active');
            $('.open_menu').toggleClass('active');
            $('.box_header .logo').toggleClass('active');
        });
    })
</script>
</head>

    
<body>
    <?php include_once('../inc/header.php'); ?>
    <div id="con_page">
        <div class="con_int store">
            <p class="tit" data-aos="fade-up" data-aos-delay="0">Vivusの商品はこちらでご購入いただけます。<br>以下フォームに内容を入力してご購入ください。<br class="view_pc-tab">なおサロン様からのご発注も、以下よりご発注を承ります。</p>
        </div>
        <div class="con_cont store">
            <article class="box_cont">
                <h2 class="tit">
                    <span>PARTNER'S STORE</span>
                    <small class="txt">パートナーストア</small>
                </h2>
                <form>
                    <fieldset class="form_info">
                        <h3 class="st">
                            <strong>購入商品</strong>
                            <small class="txt">ご希望の商品に希望数量を入力してください</small>
                        </h3>
                        <div class="box_order">
                            <ul class="box_item">
                                <li class="item">
                                    <label class="en" for="amp">
                                        <img src="../../products/regina/spicure/imgs/thum_item_7am.png" alt="">
                                        <span>7AMPOULES</span>
                                        <em class="price">6,800</em>
                                    </label>
                                    <select name="" id="">
                                        <option value="0">0</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                        <option value="9">9</option>
                                        <option value="10">10</option>
                                    </select>
                                </li>
                                <li class="item">
                                    <label class="en" for="aqua">
                                        <img src="../../products/regina/spicure/imgs/thum_item_aqua.png" alt="">
                                        <span>AQUA CREAM</span>
                                        <em class="price">8,000</em>
                                    </label>
                                    <select name="" id="">
                                        <option value="0">0</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                        <option value="9">9</option>
                                        <option value="10">10</option>
                                    </select>

                                </li>
                                <li class="item">
                                    <label class="en" for="foam">
                                        <img src="../../products/regina/spicure/imgs/thum_item_foam2.png" alt="">
                                        <span>Cleansing Foam</span>
                                        <em class="price">2,800</em>
                                    </label>
                                    <select name="" id="">
                                        <option value="0">0</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                        <option value="9">9</option>
                                        <option value="10">10</option>
                                    </select>
                                </li>
                                <li class="item">
                                    <label class="en" for="vsera">
                                        <img src="../../products/regina/spicure/imgs/thum_item_vsera.png" alt="">
                                        <span>CICA V.SERA</span>
                                        <em class="price">3,800</em>
                                    </label>
                                    <select name="" id="">
                                        <option value="0">0</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                        <option value="9">9</option>
                                        <option value="10">10</option>
                                    </select>

                                </li>
                                <li class="item">
                                    <label class="en" for="toner">
                                        <img src="../../products/regina/spicure/imgs/thum_item_attirance.png" alt="">
                                        <span>Attirance Toner</span>
                                        <em class="price">4,500</em>
                                    </label>
                                    <select name="" id="">
                                        <option value="0">0</option>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                        <option value="9">9</option>
                                        <option value="10">10</option>
                                    </select>
                                </li>
                            </ul>
                            <dl class="box_total">
                                <dt class="txt">
                                    <span>商品価格(税込・送料込)</span>
                                </dt>
                                <dd class="box_price">計<strong>28,000</strong>円</dd>
                            </dl>
                            <ul class="box_memo">
                                <li>店舗でご案内を受けた方は、店舗でご案内を受けた際にお渡しした<strong>サロンID</strong>を必ず入力してください。</li>
                                <li>入力がないと割引価格が適応されないのでご注意ください。サロンID が不明な場合は、店舗へお問い合わせください。</li>
                            </ul>
                        </div>
                    </fieldset>
                    <fieldset class="form_info">
                        <h3 class="st">
                            <i class="fas fa-truck"></i>
                            <strong>お届け先情報</strong>
                        </h3>
                        <p class="form_salon">
                            <label for="user">サロンID</label>
                            <input type="text" name="user" id="user" placeholder="サロンID">
                        </p>
                        <p class="form_double">
                            <label for="name">お名前</label>
                            <input type="text" name="name" id="name"　placeholder="お名前を入力してください。" required>
                            <input type="text" name="kana" id="name2" placeholder="フリガナ" required>
                        </p>
                        <p class="form_address">
                            <label for="address">住所</label>
                            <small class="txt">※ハイフンなしで入力してください。<br>※郵便番号を入力すると、「都道府県」「市町村」が自動入力されます。</small>
                            <input class="post" type="tel" name="post" id="address" placeholder="〒 郵便番号" required>
                            <input type="text" name="address1" id="address1" placeholder="都道府県" required>
                            <input type="text" name="address2" id="address2" placeholder="市町村" required>
                            <input type="text" name="address3" id="address3" placeholder="番地その他" required>
                        </p>
                        <p>
                            <label for="tel">電話番号</label>
                            <input type="tel" name="tel" id="tel" required>
                        </p>
                        <p>
                            <label for="mail">メールアドレス</label>
                            <input type="email" name="mail" id="mail" required>
                        </p>
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
                        <input type="submit" value="申し込みを送る">
                    </p>
                </form>            
            </article>
        </div>
        
    </div>
    <?php include_once('../inc/footer.php'); ?>

    
</body>
</html>














