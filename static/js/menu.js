$('#modetab a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})

jQuery(function($){
    $("form").submit(function(event){
        dispLoading("生成中...");
        event.preventDefault();
        var $form = $(this);
        $.ajax({
            url: $form.attr('action'),
            type: 'GET',
            data: $form.serialize(),
            beforeSend: function(xhr, settings) {
                // ボタンを無効化し、二重送信を防止
                $(".btn").attr('disabled', true);
            },
            success:function(resultdata) {
                // 指定されたデータを保持するBlobを作成する。
                var blob = new Blob([ resultdata ], { "type" : "application/x-msdownload" });
                // Aタグのhref属性にBlobオブジェクトを設定し、リンクを生成
                var a = document.createElement('a');
                a.href =  window.URL.createObjectURL(blob);
                a.download = $form.attr('id')+".txt";
                a.click();
            },
            error: function(error) {
                alert('取得に失敗しました');
            },
            complete : function(data) {
                // Loadingイメージを消す
                $(".btn").attr('disabled', false);
                removeLoading();
            }
        });
    });
});

// Loadingイメージ表示関数
function dispLoading(msg){
    // 画面表示メッセージ
    var dispMsg = "";
 
    // 引数が空の場合は画像のみ
    if( msg != "" ){
        dispMsg = "<div class='loadingMsg'>" + msg + "</div>";
    }
    // ローディング画像が表示されていない場合のみ表示
    if($("#loading").size() == 0){
        $("body").append("<div id='loading'>" + dispMsg + "</div>");
    } 
}
 
// Loadingイメージ削除関数
function removeLoading(){
    $("#loading").remove();
}