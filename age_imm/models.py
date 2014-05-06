
from django.db import models

class agenzia (models.Model):
	nomeAG = models.CharField(primary_key=True, max_length=20)
	citta = models.CharField(max_length=20)
	via = models.CharField(max_length=20)
	civico = models.CharField(max_length=20)
	provincia = models.CharField(max_length=4)
	telefono = models.CharField(max_length=12)
	email = models.CharField(max_length=20)

	def __unicode__(self):
		return u'%s, %s - %s, %s (%s) tel.%s, email:%s' % (self.nomeAG, self.citta, self.via, self.civico, self.provincia, self.telefono, self.email)

	class Meta:
		verbose_name_plural = "Agenzie"


class immobile (models.Model):
	cod_imm = models.AutoField(primary_key=True)
	zona = models.CharField(max_length=20)
	mq = models.IntegerField()
	num_camere = models.PositiveSmallIntegerField()
	num_bagni = models.PositiveSmallIntegerField()
	descrizione = models.CharField(max_length=20)
	link_foto = models.CharField(max_length=20)

	def __unicode__(self):
		return u'%s %s mq:%s c:%s b:%s %s foto:%s' % (self.cod_imm, self.zona, self.mq, self.num_camere, self.num_bagni, self.descrizione, self.link_foto)

	class Meta:
		verbose_name_plural = "Immobili"

class annuncio (models.Model):
	id_annuncio = models.AutoField(primary_key=True)
	data_a = models.DateField()
	vendita = models.IntegerField()
	nuda_pr = models.IntegerField()
	affitto = models.IntegerField()
	cessione = models.IntegerField()
	nomeAG = models.ForeignKey('agenzia')
	cod_imm = models.ForeignKey('immobile')

	def __unicode__(self):
		return u'%s data:%s [%s,%s,%s,%s] %s %s' % (self.id_annuncio, self.data_a, self.vendita, self.nuda_pr, self.affitto, self.cessione, self.nomeAG, self.cod_imm)

	class Meta:
		verbose_name_plural = "Annunci"

class utente (models.Model):
	CF = models.CharField(primary_key=True, max_length=20)
	cognome = models.CharField(max_length=20)
	nome = models.CharField(max_length=20)
	telefono = models.CharField(max_length=12)
	email = models.CharField(max_length=20)

	def __unicode__(self):
		return u'CF:%s %s %s %s %s' % (self.CF, self.cognome, self.nome, self.telefono, self.email)

	class Meta:
		verbose_name_plural = "Utenti"

class richieste (models.Model):
	id_annuncio = models.ForeignKey('annuncio')
	CF = models.ForeignKey('utente')
	data_r = models.DateField()

	class Meta:
		unique_together = (("id_annuncio_id", "CF_id"),)

	def __unicode__(self):
		return u'%s CF:%s data:%s' % (self.id_annuncio_id, self.CF_id, self.data_r)

	class Meta:
		verbose_name_plural = "Richieste"

