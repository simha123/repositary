from fabric.api import local

def test():
  local("cd /opt/fabtest/repositary && touch file1 file2 file3")
  local("cd /opt/fabtest/repositary && git add . && git commit -m test")
  local("cd /opt/fabtest/repositary && git push origin master")

