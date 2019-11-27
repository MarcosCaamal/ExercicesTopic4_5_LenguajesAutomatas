import re #libreria de expresiones regulares

path ="javascript.js"

try:
    archivo=open(path, 'r')
except:
    print("El archivo que intentas abrir no existe")
    quit()

texto=""

for linea in archivo:
    texto+=linea


patron1=re.compile('[a-zA-Z][\w\d]*')
result1=patron1.findall(texto)

patron2=r"\bconsole\b|\blog\b|\blet\b|\bvar\b|\bconst\b|\bpush\b|\bpop\b|\bunshift\b|\bshift\b|\bslice\b|\bsplice\b|\breverse\b|\bsplit\b|\bjoin\b|\bsort\b|\bindexOf\b|\bfindIndex\b|\bfind\b|\bnew\b|\bSet\b|\bof\b|\bforEach\b|\bsome\b|\bevery\b|\blenght\b|\bmap\b|\bfilter\b|\breduce\b|\btoFixed\b|\bparseInt\b|\bparseFloat\b|\bMath.random\b|\bthis\b|\bdelete\b|\bObject.getPrototypeOf\b|\bObject.assign\b|\bString.prototype\b|\bhasOwnProperty\b|\blegs\b|\blastIndex\b|\bincludes\b|\bstartsWith\b|\bendsWith\b|\breplace\b|\bsubstr\b|\breturn\b|\bprompt\b|\balert\b|\bArray\b|\bbreak\b|\bcase\b|\bcatch\b|\bclass\b|\bdefault\b|\bdo\b|\belse\b|\belseif\b|\bendsswitch\b|\beval\b|\bextends\b|\bfor\b|\bfunction\b|\bif\b|\bimplements\b|\binclude\b|\binstanceof\b|\binterface\b|\bprint\b|\bprivate\b|\bprotected\b|\bpublic\b|\brequire\b|\bstatic\b|\bswitch\b|\bthrow\b|\btry\b|\buse\b|\bwhile\b|\btrue\b|\bfalse\b"
result2=re.findall(patron2, texto)

patron3=re.compile('\d*\.?\d+')
result3=patron3.findall(texto)

patron4=re.compile('\*\*|--|\+\+|\+=|-=|/=|\%|\+|-|\*|/|=')
result4=patron4.findall(texto)

patron5=re.compile('<|<=|>|>=|==|!=')
result5=patron5.findall(texto)

for i in result1:
    if(i!="console" and i!="log" and i!="let" and i!="var" and i!="const" and i!="push" and i!="pop" and i!="unshift" and i!="shift" and i!="slice" and i!="splice" and i!="reverse" and i!="split" and i!="join" and i!="sort" and i!="indexOf" and i!="findIndex" and i!="find" and i!="new" and i!="Set"
    and i!="of" and i!="forEach" and i!="some" and i!="every" and i!="lenght" and i!="map" and i!="filter" and i!="reduce" and i!="toFixed" and i!="parseInt" and i!="parseFloat"
    and i!="Math.random" and i!="this" and i!="delete" and i!="Object.getPrototypeOf" and i!="Object.assign" and i!="String.prototype" and i!="hasOwnProperty" and i!="legs" and i!="lastIndex" and i!="includes" and i!="startsWith" and i!="endsWith"
    and i!="replace" and i!="substr" and i!="return" and i!="prompt" and i!="alert" and i!="Array" and i!="break" and i!="case" and i!="catch" and i!="class" and i!="default" and i!="do" and i!="else" and i!="elseif"
    and i!="endsswitch" and i!="eval" and i!="extends" and i!="for" and i!="function" and i!="if" and i!="implements" and i!="include" and i!="instanceof" and i!="interface" and  i!="print"
    and i!="private" and i!="protected" and i!="public" and i!="require" and i!="static" and i!="switch" and i!="throw" and i!="try" and i!="use" and i!="while" and i!="true" and i!="false"):
        print("Identificador: "+i)


for j in result2:
    print("Palabras reservadas: "+j)

for j in result3:
    print("Números: "+j)
 
 

for k in result4:
    print("Operadores aritméticos: "+k)


for l in result5:
    print("Operadores relacionales: "+l)




