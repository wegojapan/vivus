<!doctype html>
<html>
<head>
<?php include "../inc/gtag.php"; ?>    
<?php include "../inc/meta.php"; ?>

     
<title>Title</title>
    
<!-- CSS Link --> 
<link rel="stylesheet" href="../css/cssName.css"/>
    
<!-- JS Link -->    
    
    
<?php include "../inc/config.php"; ?>
<?php include "../inc/head.php"; ?>    
<?php include "../inc/include_slick.php"; ?>
    
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
        contents
        
    </div>
    <?php include_once('../inc/footer.php'); ?>

    
</body>
</html>














