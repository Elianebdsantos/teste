import mysql.connector
import smtplib
import email.message
import schedule
import time


def buscar_dados():
    # Conectar ao banco de dados
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="senai@134",
        db="bd_medidor"
    )
    
    cursor = conn.cursor()
    query = "SELECT temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro FROM tb_registro"
    cursor.execute(query)
    
    # Obter os dados
    registros = cursor.fetchall()
    cursor.close()
    conn.close()

    return registros


def criar_corpo_email(registros):
    corpo_email = "<h2>Indicadores de Sensores</h2>"
#    for registro in registros:
#        temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro = registro
#        corpo_email += f"""
#        <p>Data: {tempo_registro}</p>
#        <ul>
#            <li>Temperatura: {temperatura} °C</li>
#            <li>Pressão: {pressao} Pa</li>
#            <li>Altitude: {altitude} m</li>
#            <li>Umidade: {umidade} %</li>
#            <li>CO2: {co2} ppm</li>
#            <li>Poeira: {poeira} µg/m³</li>
#        </ul>
#        <hr>
#        """
    temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro = registros[0]
    corpo_email = f"""
    <p>Data: {tempo_registro}</p>
    <ul>
        <li>Temperatura: {temperatura} °C</li>
        <li>Pressão: {pressao} Pa</li>
        <li>Altitude: {altitude} m</li>
        <li>Umidade: {umidade} %</li>
        <li>CO2: {co2} ppm</li>
        <li>Poeira: {poeira} µg/m³</li>
    </ul>
    <hr>
    """
    return corpo_email


def enviar_email(corpo_email):
    msg = email.message.Message()
    msg['Subject'] = "Indicadores de Sensores"
    msg['From'] = 'projetosenai.cd24@gmail.com'
    msg['To'] = 'clodoaldo.batista.s@gmail.com, eliane.bdsantos@gmail.com'
    password = "cdol xorh tmlf inpz"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'].split(','), msg.as_string().encode('utf-8'))
    s.quit()
    print("Email enviado")


if __name__ == "__main__":
    registros = buscar_dados()
    corpo_email = criar_corpo_email(registros)
    enviar_email(corpo_email)

#schedule.every().day.at("20:56").do()

#while True:
#    schedule.run_pending()  
#    time.sleep(1)