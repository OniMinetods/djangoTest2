fetch('http://127.0.0.1:8000/news/data')
  .then((response) => {
    if (!response.ok) {
      throw new Error('Error occurred!');
    }
    return response.json();
  })
  .then((data) => {
    console.log(data);
  })
  .catch((err) => {
    errorMessage(err);
  });
