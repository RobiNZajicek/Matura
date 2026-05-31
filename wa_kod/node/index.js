const http = require('http')
const server= http.createServer((req,resp)=>{
    resp.write('Ahoj')
    resp.end()
})
server.listen(3000)