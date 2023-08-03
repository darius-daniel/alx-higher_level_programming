const url = 'https://www.fourtonfish.com/hellosalut/hello/';

window.onload = function () {
  $('INPUT#btn_translate').click(() => {
    showHello();
  });
  $('INPUT#language_code').keypress((event) => {
    if (event.keyCode === 13) {
      showHello();
    }
  });
};

function showHello () {
  const lan = $('INPUT#language_code').val();
  $.get(url + lan, (data) => {
    $('DIV#hello').text(data.hello);
  });
}
