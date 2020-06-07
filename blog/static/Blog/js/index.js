$(function(){
	var overflow_hidden = $(".overflow-hidden");
	var returnTop = $("#returnTop")
	var container = $(".container")
	var $like = $(".like")
	var $eye_open = $(".eye-open")
	var $comments = $(".comments")
	var $closer = $(".remove")
	{
		$("hearder").css({"height":$(window).innerHeight()+"px"});
	}
	overflow_hidden.each(function(){
		$(this).mouseover(function(){
			$(this).find("span").clearQueue();
			$(this).find("span").animate({left:"100%"},500,function(){
				$(this).find("span").css({left:"100%"})
			});
		})
		$(this).mouseout(function(){
			$(this).find("span").clearQueue();
			$(this).find("span").animate({left:"250%"},500,function(){
				$(this).css({"left":"-16px"})	
			});
		})
	})
	
	$(window).scroll(function(event){
		let scroll_top = $(this).scrollTop();
		if(scroll_top>$("nav").innerHeight()){
			$("nav").css({"position":"fixed","background-color":"black"});
		}else{
			$("nav").css({"position":"absolute","background-color":"rgba(0,0,0,0)"})
			$("nav").clearQueue()
		}
		if(scroll_top>$(window).innerHeight()){
			returnTop.clearQueue()
			returnTop.animate({right:"100px"},500);
		}else{
			returnTop.clearQueue()
			returnTop.animate({right:"-100%"},500);
		}
	});
	returnTop.click(function(){
		$("html,body").animate({scrollTop:"0"},500);
	})
	// 关闭
	$closer.click(function(){
		if(confirm("确定删除？")){
			$(this).parent().parent().parent().remove()
		}
	})
	// 点赞
	$like.click(function(){
		let like_counter_node = $(this).parent().children(".like-counter");
		let like_id = parseInt($(this).parent().parent().children(".hide-id").html());
		// $(this).toggleClass("icon-zan-copy-copy")
		// $(this).toggleClass("icon-dianzan_active")
		$(this).toggleClass("blue")
		if($(this).hasClass("blue")){
			$.ajax({
				  url: '',
				  type: 'post',
				  // 设置的是请求参数
				  data: { id: like_id, like: '1'},
				  // 用于设置响应体的类型 注意 跟 data 参数没关系！！！
				  dataType: 'json',
				  success: function (res) {
					// 一旦设置的 dataType 选项，就不再关心 服务端 响应的 Content-Type 了
					// 客户端会主观认为服务端返回的就是 JSON 格式的字符串
						like_counter_node.html(parseInt(like_counter_node.html())+1);
				  }
			})
		}else{
			$.ajax({
				  url: '',
				  type: 'post',
				  // 设置的是请求参数
				  data: { id: like_id, scan:'0'},
				  // 用于设置响应体的类型 注意 跟 data 参数没关系！！！
				  dataType: 'json',
				  success: function (res) {
					// 一旦设置的 dataType 选项，就不再关心 服务端 响应的 Content-Type 了
					// 客户端会主观认为服务端返回的就是 JSON 格式的字符串
						like_counter_node.html(parseInt(like_counter_node.html())-1);
				  }
			})
		}
	})
	// 标记已经浏览
	$eye_open.click(function(){
		let scan_counter_node = $(this).parent().children(".eyeopen-counter");
		let like_id = parseInt($(this).parent().parent().children(".hide-id").html());
		$(this).toggleClass("blue")
		if($(this).hasClass("blue")){
			$.ajax({
				  url: '',
				  type: 'post',
				  // 设置的是请求参数
				  data: { id: like_id, scan: '1'},
				  // 用于设置响应体的类型 注意 跟 data 参数没关系！！！
				  dataType: 'json',
				  success: function (res) {
					// 一旦设置的 dataType 选项，就不再关心 服务端 响应的 Content-Type 了
					// 客户端会主观认为服务端返回的就是 JSON 格式的字符串
						scan_counter_node.html(parseInt(scan_counter_node.html())+1);
				  }
			})
		}else{
			$.ajax({
				  url: '',
				  type: 'post',
				  // 设置的是请求参数
				  data: { id: like_id, scan:'0'},
				  // 用于设置响应体的类型 注意 跟 data 参数没关系！！！
				  dataType: 'json',
				  success: function (res) {
					// 一旦设置的 dataType 选项，就不再关心 服务端 响应的 Content-Type 了
					// 客户端会主观认为服务端返回的就是 JSON 格式的字符串
						scan_counter_node.html(parseInt(scan_counter_node.html())-1);
				  }
			})
		}
	})
})