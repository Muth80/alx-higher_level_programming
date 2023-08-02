$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    if (languageCode !== '') {
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`;
      $.get(apiUrl, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});

