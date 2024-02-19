const express = require('express');
const http = require('http');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

app.use(express.static('public')); // Serve your frontend files

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    // Handle incoming messages from clients
    console.log('received: %s', message);
  });

  // Example of sending a message to all connected clients
  const updateTxtContent = (content) => {
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(content);
      }
    });
  };

  // You would call updateTxtContent whenever you have new .txt content to push
});

server.listen(3000, () => {
  console.log('Server started on port 3000');
});
