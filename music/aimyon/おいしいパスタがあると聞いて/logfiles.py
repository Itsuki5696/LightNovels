import os

dir_path = os.path.dirname(os.path.realpath(__file__))

music_list = []

for filename in os.listdir(dir_path):
    if (filename.endswith(".mp3")):
        files = filename.split('.')
        id_str = "{id: " + str(int(files[0])) + ", name: '" + files[1] + "', author: 'あいみょん', album: 'おいしいパスタがあると聞いて', keywords: ['aimyon', '爱谬'], type: 'music', cover: 'https://github-resources.itsuki.de/music/aimyon/おいしいパスタがあると聞いて/cover.jpg', file: 'https://github-resources.itsuki.de/music/aimyon/おいしいパスタがあると聞いて/" + filename + "', year: 2020, description: ''}"
        music_list.append(id_str)

print(','.join(music_list))
