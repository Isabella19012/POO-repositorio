import sqlite3

class Database:
    conn = None
    nome_bd="agenda.db"

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")
 
    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()

    @classmethod
    def criar_tabelas(cls):
        # --------------------- Tabela Cliente ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                fone TEXT,
                id_convenio INTEGER,

                FOREIGN KEY (id_convenio) REFERENCES Convenio(id) ON DELETE CASCADE
            );
        """)

        # --------------------- Tabela Profissional ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Profissional (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                especializacao TEXT NULL,
                senha TEXT NOT NULL
            );
        """)

        # --------------------- Tabela Servico ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL
            );
        """)

        # --------------------- Tabela Horario ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Horario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                confirmado INTEGER DEFAULT 0,
                id_cliente INTEGER,
                id_servico INTEGER,
                id_profissional INTEGER,

                FOREIGN KEY (id_cliente) REFERENCES Cliente(id) ON DELETE CASCADE,
                FOREIGN KEY (id_servico) REFERENCES Servico(id) ON DELETE CASCADE,
                FOREIGN KEY (id_profissional) REFERENCES Profissional(id) ON DELETE CASCADE
            );
        """)

        # --------------------- Tabela Atendimento ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Atendimento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                queixa_principal TEXT NULL,
                historico_saude TEXT NULL,
                avaliacao TEXT NULL,
                prescricao TEXT NULL,
                id_horario INTEGER,
                pago INTEGER DEFAULT 0,
                total REAL NOT NULL,

                FOREIGN KEY (id_horario) REFERENCES Horario(id) ON DELETE CASCADE
            );
        """)
            # --------------------- Tabela Convenio ---------------------
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Convenio (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                contato TEXT NOT NULL,
                fone TEXT
            );
        """)
if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()
