import cv2
 
#Cargamos nuestro classificador de Haar: --> Para entrenar a la AI
cascada_rostro = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#Iniciar la webcam:
webcam = cv2.VideoCapture("shai2.mp4")
# NOTA 1: Si no funciona puedes cambiar el índice 0 por otro, o cambiarlo por la dirección de tu webcam (p.ej. '/dev/video0')
# NOTA 2: también debería funcionar si en vez de una webcam utilizas un fichero de vídeo.
print("\nRecordatorio: pulsa 'ESC' para cerrar.\n")
 
while(1):
 
    #Capturar una imagen con la webcam:
    valido, img = webcam.read()
 
    #Si la imagen es válida (es decir, si se ha capturado correctamente), continuamos:
    if valido:
        #Convertir la imagen a gris:
        img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Buscamos los rostros:
        coordenadas_rostros = cascada_rostro.detectMultiScale(img_gris, 1.3, 5)
        #Recorremos el array 'coordenadas_rostros' y dibujamos los rectángulos sobre la imagen original:
        for (x,y,ancho, alto) in coordenadas_rostros:
            cv2.rectangle(img, (x,y), (x+ancho, y+alto), (0,0,255) , 3)
        #Abrimos una ventana con el resultado:
        cv2.imshow('Output', img)
        #Salir con 'ESC':
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
            break

webcam.release()