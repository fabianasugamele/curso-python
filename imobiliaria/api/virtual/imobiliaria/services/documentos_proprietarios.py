from configs.db import db
from entities.documentos_proprietario import DocumentosProprietario

class ServiceDocumentosProprietario():
    def save(request):
        documentos_proprietario = DocumentosProprietario(request.json['cpf'], request.json['rg'], request.json['titulo_eleitoral'])
        db.session.add(documentos_proprietario)
        db.session.commit()