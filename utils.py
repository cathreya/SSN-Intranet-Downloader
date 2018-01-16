import git
import datetime
import glob

r = git.Repo('.')
remote_parts = r.remotes.origin.url[:-4].split('/')
uname = remote_parts[3]

curr = 'file://' + os.getcwd()
newpath = 'https://' + uname + '.github.io/SSN-Intranet-Downloader'

allhtmls = glob.glob('*/*/*.html') + glob.glob('*/*.html')
for f in allhtmls:
    fl = open(f)
    content = fl.read()
    content = content.replace(curr, newpath)
    open(f, 'w').write(content)

r.index.add(['CseElearnThirdYear/*'])
r.index.commit('Added files - ' + str(datetime.datetime.now()))
