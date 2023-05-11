import csv

global escritor
escritor = open("registro-de-artesanos-alimentarios.rdf", "w", encoding='utf-8')
global i
i = 1


def escribeLinea(texto=""):
    escritor.write(texto + "\n")

def escribirOrganizacion(department, identifier, legalName, taxID, telephone, faxNumber, email, relatedLink, status):
    escribeLinea(":" + "".join(identifier.split('/')[1].split("-")) + " a schema:Organization;")
    escribeLinea('  schema:department "' + department + '";')
    escribeLinea('  schema:identifier "' + identifier + '";')
    escribeLinea('  schema:legalName "' + legalName + '";')
    escribeLinea('  schema:taxID "' + taxID + '";')
    if len(telephone) != 0:
        escribeLinea('  schema:telephone "' + telephone + '";')
    if len(faxNumber) != 0:
        escribeLinea('  schema:faxNumber "' + faxNumber + '";')
    if len(email) != 0:
        escribeLinea('  schema:email "' + email + '";')
    if len(relatedLink) != 0:
        escribeLinea('  schema:relatedLink "' + relatedLink + '";')
    escribeLinea('  schema:status "' + status + '";')
    escribeLinea('  schema:address _:a' + str(i) + ';')
    escribeLinea('  schema:workLocation _:p' + str(i) + '.')
    escribeLinea()


def escribirPersona(telephone):
    if len(telephone) != 0:
        escribeLinea("_:p" + str(i) + " a schema:Person;")
        escribeLinea('  schema:telephone "' + telephone + '" .')
    else:
        escribeLinea("_:p" + str(i) + " a schema:Person .")
    escribeLinea()


def escribirLocalizacion(streetAddress, postalCode, addressLocality, addressRegion, provinceCode):
    escribeLinea("_:a" + str(i) + " a schema:PostalAddress;")
    escribeLinea('  schema:streetAddress "' + streetAddress + '";')
    escribeLinea('  schema:postalCode "' + postalCode + '";')
    escribeLinea('  schema:addressLocality "' + addressLocality + '";')
    escribeLinea('  schema:addressRegion dbr:' + addressRegion + ';')
    escribeLinea('  :provinceCode "' + provinceCode + '" .')
    escribeLinea()


def escribirArtesanos(abreviaturas):
    escribeLinea(":foodArtisans a schema:RegisterAction;")
    escribeLinea('  schema:participant ' + ",".join(abreviaturas) + ';')
    escribeLinea('  schema:location dbr:España .')
    escribeLinea()


def escribirComienzo():
    escribeLinea("@prefix sc: <http://purl.org/science/owl/sciencecommons/> .")
    escribeLinea("prefix :       <http://example.org/>")
    escribeLinea("prefix schema: <http://schema.org/>")
    escribeLinea("prefix dbr:    <http://dbpedia.org/resource/>  ")
    escribeLinea()


with open('registro-de-artesanos-alimentarios.csv', 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=';')
    escribirComienzo()
    abreviaturas = []
    for linea in lector_csv:
        abreviaturas.append(':' + "".join(linea[1].split('/')[1].split("-")))
        escribirOrganizacion(linea[0], linea[1], linea[2], linea[3], linea[8], linea[10], linea[11], linea[12], linea[13])
        escribirPersona(linea[9])
        escribirLocalizacion(linea[4], linea[5], linea[6], linea[7], linea[14])
        i = i + 1
    escribirArtesanos(abreviaturas)
