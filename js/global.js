$OBJ = {
	'win' : $(window),
	'doc' : $(document),
	'html' : $('html')
}

function winW(){//창 너비
	return $OBJ.win.width();
}

function winH(){// 창 높이
	return $OBJ.win.height();
}

function winSh(){// 스크롤 값
	return $OBJ.win.scrollTop();
}


function mChk(){// 모바일 체크
	return $('#mchk').is(':visible');
}

var head = {
	init : function(){
		this.action();
	},
	action : function(){
		var a = $('#header');
		var gnb = a.find('.gnb');

		gnb.on('mouseenter',function(){
			$OBJ.html.addClass('gnbOn');
		}).on('mouseleave',function(){
			$OBJ.html.removeClass('gnbOn');
		}).on('click','> li > a',function(){
			if(mChk() == true || $(this).next('ul').length > 0){
				$(this).closest('li').toggleClass('active').siblings().removeClass('active');
				return false;
			}
		});

		$('#mchk').on('click',function(){
			$OBJ.html.toggleClass('gnbOn');
		});

		$('#aside .btn1 a').on('click',function(){
			$(this).closest('.btn1').toggleClass('active');
			return false;
		});

		function headShadow(){
			if(winSh() > 50){
				$OBJ.html.addClass('headShadow');
			}else{
				$OBJ.html.removeClass('headShadow');
			}
		}

		$OBJ.win.on('load scroll',function(){
			headShadow();
		});
	}
};


var main = {
	init : function(){
		this.action();
	},
	action : function(){
		var visSwiper = new Swiper('#vis', {
			loop: true,
			effect: 'fade',
			speed: 1000,
			pagination: {
				el: '#vis .num',
				type: 'fraction',
			},
			navigation: {
				nextEl: '#vis .next',
				prevEl: '#vis .prev',
			},
			autoplay: {
				delay: 5000,
				disableOnInteraction: false,
			},
			on: {
				slideChangeTransitionEnd: function () {
					$('#vis .progress').addClass('active');
				},
				slideChangeTransitionStart: function () {
					$('#vis .progress').removeClass('active');
				}
			}
		});

		var commSwiper = new Swiper('#comm .swiper-container', {
			effect: 'fade',
			speed: 1000,
			navigation: {
				nextEl: '#comm .next',
				prevEl: '#comm .prev',
			},
			autoplay: {
				delay: 5000,
				disableOnInteraction: false,
			}
		});

	}
};


var snb = {
	init : function(){
		if($('#snb').length > 0){
			this.action();
		}
	},
	action : function(){
		$('#snb .ov > span').on('click',function(){
			$(this).closest('.ov').toggleClass('active').siblings().removeClass('active');
		});
	}
};

var tab = {
	init : function(){
		if($('._tab').length > 0){
			this.action();
		}
	},
	action : function(){
		$('._tab').on('click','> *',function(){
			$(this).addClass('active').siblings().removeClass('active');
			$('._tabbox').eq($(this).index()).addClass('active').siblings().removeClass('active');
			return false;
		});
	}
};

$OBJ.doc.ready(function(){
	head.init();
	snb.init();
	tab.init();
});

$OBJ.win.on('load',function(){
	AOS.init({
		duration:1000,
		offset: 20
	});
});

// TAB
$(function(){
    var $tab = $('#tab'),
        $li = $tab.find('li'),
        $select = $tab.find('select');

    $li.click(function(){
        var target = $(this).attr('data-target');
        if($(target).is(':hidden')) {
            $(target).fadeIn(300).siblings().hide();
            $(this).addClass('active').siblings().removeClass('active');
            $select.val(target);
        }
    });

    $select
    .prop('selectIndex',1)
    .change(function(){
        var i = $(this).prop('selectedIndex');
        $li.eq(i).trigger('click');
    });
});