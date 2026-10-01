from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from reportlab.pdfgen import canvas

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return {
        "mensagem": "API Python funcionando!"
    }

@app.route("/certificado", methods=["POST"])
def certificado():

    dados = request.get_json(force=True, silent=True)

    if not dados:
        return jsonify({
            "erro": "Nenhum dado JSON foi enviado."
        }), 400

    nome = dados.get("nome")
    curso = dados.get("curso")
    carga = dados.get("cargaHoraria")

    if not nome or not curso or not carga:
        return jsonify({
            "erro": "Nome, curso e carga horária são obrigatórios."
        }), 400

    arquivo = "certificado.pdf"

    pdf = canvas.Canvas(
        arquivo,
        pagesize=(842, 595)
        )

# Cores
    azul = "#1d4ed8"
    cinza = "#475569"

# Fundo branco
    pdf.setFillColorRGB(1, 1, 1)
    pdf.rect(0, 0, 842, 595, fill=1, stroke=0)

# Borda externa
    pdf.setStrokeColor(azul)
    pdf.setLineWidth(4)
    pdf.rect(
    25,
    25,
    792,
    545,
    fill=0,
    stroke=1
)

    # Borda interna
    pdf.setStrokeColorRGB(0.7, 0.8, 0.95)
    pdf.setLineWidth(1)
    pdf.rect(
    40,
    40,
    762,
    515,
    fill=0,
    stroke=1
)
    
    # Símbolo
    pdf.setFillColor(azul)
    pdf.setFont("Helvetica-Bold", 28)
    pdf.drawCentredString(
    421,
    500,
    "★"
)

# Título
    pdf.setFillColor(azul)
    pdf.setFont("Helvetica-Bold", 30)
    pdf.drawCentredString(
    421,
    450,
    "CERTIFICADO"
)

# Linha decorativa
    pdf.setStrokeColor(azul)
    pdf.setLineWidth(2)
    pdf.line(
    260,
    425,
    582,
    425
)

# Texto
    pdf.setFillColor(cinza)
    pdf.setFont("Helvetica", 16)

    pdf.drawCentredString(
    421,
    375,
    "Certificamos que"
)

# Nome
    pdf.setFillColorRGB(0.05, 0.1, 0.2)
    pdf.setFont("Helvetica-Bold", 26)

    pdf.drawCentredString(
    421,
    330,
    nome
)

# Texto do curso
    pdf.setFillColor(cinza)
    pdf.setFont("Helvetica", 16)

    pdf.drawCentredString(
    421,
    285,
    "concluiu com aproveitamento o curso"
)

# Curso
    pdf.setFillColor(azul)
    pdf.setFont("Helvetica-Bold", 21)

    pdf.drawCentredString(
    421,
    245,
    curso
)

# Carga horária
    pdf.setFillColor(cinza)
    pdf.setFont("Helvetica", 14)

    pdf.drawCentredString(
    421,
    200,
    f"Carga horária: {carga}"
    )

# Data
    from datetime import datetime

    data = datetime.now().strftime("%d/%m/%Y")

    pdf.setFont("Helvetica", 12)

    pdf.drawCentredString(
    421,
    100,
    f"Emitido em {data}"
    )

# Assinatura
    pdf.setStrokeColorRGB(0.3, 0.3, 0.3)
    pdf.setLineWidth(1)

    pdf.line(
    310,
    75,
    532,
    75
    )

    pdf.setFillColor(cinza)
    pdf.setFont("Helvetica", 10)

    pdf.drawCentredString(
    421,
    60,
    "Sistema de Certificados"
    )

    pdf.save()

    return send_file(
        arquivo,
        as_attachment=True,
        download_name="certificado.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )