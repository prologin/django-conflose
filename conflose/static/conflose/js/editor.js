django.jQuery(function() {
    var editor = ace.edit('editor_css');
    editor.session.setOptions({
        mode: "ace/mode/css",
        tabSize: 2,
        useSoftTabs: true
    });

    var textarea = django.jQuery('textarea[name="css"]');
    editor.getSession().on("change", function () {
        textarea.val(editor.getSession().getValue());
    });
});
