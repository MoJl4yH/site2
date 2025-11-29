from livereload import Server

server = Server()

# Следить рекурсивно за всеми файлами
server.watch('**/*', delay=0.2)

server.serve(root='.', port=5500)
