const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (response) => {
  const movies = response.results;
  $(document).ready(() => {
    for (const movie of movies) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    }
  });
});
