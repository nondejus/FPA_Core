!function(e){e(document).ready(function(){e(".expandbtn").click(function(){e(this).hasClass("expanded")?(e(this).removeClass("expanded").html("<<"),e(".popupcontainer").hide(),e(".warningmessage").hide(),e.cookie("shownfeedback",!0)):(e(this).addClass("expanded").html(">>"),e(".popupcontainer").show())});var n=e.cookie("shownfeedback");n&&(e(".expandbtn").click(),e(".warningmessage").hide()),e("#feedbackform").submit(function(n){e("#feedbackbtn").hide();var a=e(this).serialize()+"&url="+window.location.href;return e.ajax({type:"POST",url:"/feedback",data:a,cache:!1,success:function(n){n.success?e(".popupcontainer").html("Thank you for your feedback."):e(".popupcontainer").html("Sorry we hit an error.  This will be noted and fixed")},error:function(){e(".popupcontainer").html("Sorry we hit an error.  This will be noted and fixed")}}),n.preventDefault(),!1})})}(jQuery);