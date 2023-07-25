import enum

from django.db import models
# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=30)
    estatura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.DecimalField(max_digits=3, decimal_places=2)

class Jugador (Persona):
    deporteProfesion = models.CharField(max_length=30)

    def inscribirDeporte(Inscripcion):
        return

    def __str__(self):
        return self.nombre

class Regla (models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class juegoPorTiempo (models.Model):
    tiempo = models.IntegerField()

class juegoPorPuntosTiempo (models.Model):
    puntos = models.IntegerField()
    numSets = models.IntegerField()
    tiempoMaxSet = models.IntegerField()

class Reglamento (models.Model):
    nombre = models.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.regla_list = None

    def aniadirRegla(self, regla):
        self.regla_list.append(regla)

    def eliminarRegla(self, regla):
        self.regla_list.remove(regla)

    def comprobarRegla(self, regla):
        return regla in self.regla_list

    def __str__(self):
        return self.nombre

class Formato (enum.Enum):
    ELIMINACION = 'ELIMINACION'
    TODOS_CONTRA_TODOS = 'TODOS_CONTRA_TODOS'
    SISTEMA_SUIZO = 'SISTEMA_SUIZO'
    GRUPOS = 'GRUPOS'
    MIXTO = 'MIXTO'

class Deporte (models.Model):
    nombre = models.CharField(max_length=30)
    numParticipantes = models.IntegerField()
    numParticipantesEncuentro = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

class DeporteIndividual (Deporte):

    def __str__(self):
        return self.nombre

class DeporteEquipo (Deporte):
    numJugadoresEquipo = models.IntegerField()

    def __str__(self):
        return self.nombre

class Equipo (models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    alineacion = models.CharField(max_length=100)

    def actualizarAlineacion(self, alineacion):
        pass
    def __str__(self):
        return self.nombre

class Estadistica (models.Model):
    encuentrosTotalesGanados: models.IntegerField()
    encuentrosTotalesPerdidos: models.IntegerField()
    encuentrosTotalesEmpatados: models.IntegerField()
    rachaVictorias: models.IntegerField()
    competenciasGanadas: models.IntegerField()
    competenciasPerdidas: models.IntegerField()

    def actualizarEstadistica (self, estadistica):
        pass

class Temporada (models.Model):
    nombre = models.CharField(max_length=30)
    periodoInicio = models.DateField()
    periodoFin = models.DateField()

    def agregarGrupo (self, grupo):
        pass

    def agregarCompetencia (self, competencia):
        pass

    def __str__(self):
        return self.nombre

class Inscripcion (models.Model):
    deporte = Deporte(models.Model)
    temporada = Temporada(models.Model)
    equipo = Equipo(models.Model)

class Competencia (models.Model):
    nombre = models.CharField(max_length=30)
    periodoFechaInicio = models.DateField()
    periodoFechaFin = models.DateField()

    def __str__(self):
        return self.nombre

class Grupo (models.Model):
    nombre = models.CharField(max_length=30)

    def asignarParticipante (self, participante):
        pass

class Noticia (models.Model):
    titulo = models.CharField(max_length=30)
    fecha = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    informacion = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Grupo (models.Model):
    nombre = models.CharField(max_length=30)

class Participante (models.Model):
    identificador = models.CharField(max_length= 30)
    puntos = models.IntegerField()
    posicion = models.IntegerField()

    def actualizarPosicion(self, posicion):
        self.posicion = posicion

class TablaPosicion (models.Model):
    posicionList = models.ManyToManyField(Participante)
    encuentrosTotalesjugados = models.IntegerField()

    def actualizarTabla(self, participante):
        self.posicionList.append(participante)

    def calcular_posiciones(participante_list):
        participante_list.sort(key=lambda p: p.puntos, reverse=True)
        for i in range(len(participante_list)):
            participante = participante_list[i]
            participante.set_posicion(i + 1)

class Estado (enum.Enum):
    INICIADO = 'INICIADO'
    SUSPENDIDO = 'SUSPENDIDO'
    ENTRE_TIEMPO = 'ENTRE_TIEMPO'
    FINALIZADO = 'FINALIZADO'
    APLAZADO = 'APLAZADO'
    NO_INICIADO = 'NO_INICIADO'

class Encuentro (models.Model):
    hayMarcador = models.BooleanField()

    def definirFecha(self, fecha):
        self.fecha = fecha

    def actualizarEstado(self, estado):
        self.estado = estado

    class Resultado(models.Model):
        ganador = Participante(models.Model)
        perdedorList = models.ManyToManyField(Participante)
        descripcion = models.CharField(max_length=100)

        def definirGanador(self, ganador):
            self.ganador = ganador

        def agregarPerdedor(self, perdedor):
            self.perdedorList.append(perdedor)

        def empate(self):
            self.ganador = None

class Marcador (models.Model):
    puntaje = models.IntegerField()
    tiempo = models.TimeField()

    def actualizarMarcador(self, puntaje):
        self.puntaje = puntaje

class Prediccion (models.Model):
    posibleResultado = Encuentro.Resultado(models.Model)
    porsentajeApostadores = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def actualizarPorcentajeApostadores(self, porcentaje):
        self.porsentajeApostadores = porcentaje

class Apuesta (models.Model):
    valorApostado = models.IntegerField()

    def apostar(self, prediccion):
        self.prediccion = prediccion

    def confirmarApuesta(self):
        self.apuestaConfirmada = True

class Fecha(models.Model):
    fechaAsignada = models.DateField()
    horaAsignada = models.TimeField()

    def __str__(self):
        return self.fechaAsignada, self.horaAsignada

class Calendario (models.Model):
    fechaList = models.ManyToManyField(Fecha)

    def aniadirFecha(self, fecha):
        self.fechaList.append(fecha)

    def eliminarFecha(self, fecha):
        self.fechaList.remove(fecha)

    def compruebaFecha(self, fecha):
        return fecha in self.fechaList

    def __str__(self):
        return self.fechaList
        
