const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
window.onload = () => {
  $.get(url, (response) => {
    $('DIV#hello').text(`${response.hello}`);
  });
};
