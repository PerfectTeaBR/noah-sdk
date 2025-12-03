#  _   _                 _
# | \ | |  ___    __ _  | |__
# |  \| | / _ \  / _` | | '_ \
# | |\  | | (_) | | (_| | | | | 
# |_| \_| \___/  \__,_| |_| |_| S D K ;w;


from noah import NoahSec, OAuthSimple

Noah = (OAuthSimple)

noah = Noah(__name__)

# Coloque no ("") o nome do seu Padrão de OAuth!
@noah.auth("teste")
def teste():
  noah.sec.define(oauth_name.define)
  return OAuthSimple ("")

if __name__=="__oauth__":
    noah.run()