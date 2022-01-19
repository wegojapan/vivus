<!doctype html>
<html>
<head>
<?php include "../inc/gtag.php"; ?>    
<?php include "../inc/meta.php"; ?>

     
<title>Vivus Contact</title>
    
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
        <div class="con_int">
            <p class="tit" data-aos="fade-up" data-aos-delay="0"><a href="../faq">よくある質問</a>ページで<br class="view_sp">解決できませんでしたか。<br>以下のフォームから<br class="view_sp">お問い合わせ下さい。</p>
        </div>
        <div class="con_cont">
            <article class="box_cont">
                <h2 class="tit">
                    <span>CONTACT</span>
                    <small class="txt">お問い合わせ</small>
                </h2>
                <p class="st">入力項目はすべて必須項目になります</p>
                <form>
                    <fieldset class="form_info">
                        <p class="form_name">
                            <label for="name">お名前</label>
                            <input type="text" name="name" id="name"　placeholder="お名前を入力してください。" required>
                            <input type="text" name="kana" id="name2" placeholder="フリガナ" required>
                        </p>
                        <p>
                            <label for="mail">メールアドレス</label>
                            <input type="email" name="mail" id="mail" required>
                        </p>
                        <p>
                            <label for="tel">電話番号</label>
                            <input type="tel" name="tel" id="tel" required>
                        </p>
                        <p>
                            <label for="msg">お問い合わせ内容</label>
                            <textarea name="msg" id="msg" cols="30" rows="5" required></textarea>
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
                        <input type="submit" value="送信する">
                    </p>
                </form>            
            </article>
        </div>
        
    </div>
    <?php include_once('../inc/footer.php'); ?>

    
</body>
</html>














