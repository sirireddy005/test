const express = require('express');
const app = express();
app.get('/user', (req, res) => {
  res.send("User data");
});
app.listen(3000);
