$(function () {
    $('#jstree').jstree({
        'core' : {
             'url' : 'doraemon.json', // ajaxで読み込むjsonファイル
             'dataType' : 'json',     // Webサーバがない状態でも読み込むために追加（chromeではこれをつけてもNG）
             'data' : function(node) { // 正直何してるかわからない
                 return {'id', node.id };
             }
         }
    }
})
.on("select_node.jstree", function(e, data) {
    // 選択されたノードの情報を取得・出力
    console.log(data.node.id); // 自動で割り当てられる
    console.log(data.node.text); // ノード名（jsonで定義した名前）
    console.log(data.node.a_attr.test_data); // a_attr（jsonで定義した値）
    /*
     * aタグ内にliタグが作成される。
     * a_attrて定義した内容はaタグ内の属性として定義される
     */
})
.on("changed.jstree", function(e, data) {
    // 変更されたノードの情報を取得・出力
 
    /*
       変更時のみ本イベントが呼び出されると思っていたが、変更されなくても
       呼び出されてた。ほゎ～～～い～なぜに～～
     */
 
    console.log(data.node.id); // 自動で割り当てられる
    console.log(data.node.text); // ノード名（jsonで定義した名前）
    console.log(data.node.a_attr.test_data); // a_attr（jsonで定義した値）
});