from configs.db import db
from entities.documentos_proprietario import DocumentosProprietario

class ServiceDocumentosProprietario():
    @staticmethod
    def save(request):
        documentos_proprietario = DocumentosProprietario()
        documentos_proprietario.set_cpf(request.json['cpf'])
        documentos_proprietario.set_rg(request.json['rg'])
        documentos_proprietario.set_titulo(request.json['titulo_eleitoral'])

    
        db.session.add(documentos_proprietario)
        db.session.commit()

    def find_all():
        return DocumentosProprietario.query.all()

    @staticmethod
    def delete(request):
        obj = DocumentosProprietario.query.filter_by(id=request.json['id']).one()
        db.session.delete(obj)
        db.session.commit()