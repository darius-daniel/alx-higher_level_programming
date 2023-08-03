const url = 'https://www.fourtonfish.com/hellosalut/hello/';

window.onload = () => {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.get(url + lan, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
};
