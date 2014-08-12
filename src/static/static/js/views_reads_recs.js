$(document).ready(function(){
    $("#views_li").addClass('is-active')
    $("#top_reads_table").hide();
    $("#top_recs_table").hide();

  $("#views_button").click(function(){
    $("#views_li").addClass('is-active')
    $("#reads_li").removeClass('is-active')
    $("#recs_li").removeClass('is-active')

    $("#top_views_table").show()
    $("#top_recs_table").hide();
    $("#top_reads_table").hide();
  });
    $("#reads_button").click(function(){
    $("#reads_li").addClass('is-active')
    $("#views_li").removeClass('is-active')
    $("#recs_li").removeClass('is-active')
    
    $("#top_reads_table").show()
    $("#top_recs_table").hide();
    $("#top_views_table").hide();
  });
    
    $("#recs_button").click(function(){
    $("#recs_li").addClass('is-active')
    $("#reads_li").removeClass('is-active')
    $("#views_li").removeClass('is-active')
    
    $("#top_recs_table").show()
    $("#top_views_table").hide();
    $("#top_reads_table").hide();
  });
  
});