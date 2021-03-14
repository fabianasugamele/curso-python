CREATE TABLE public.tipos_imovel (
	id serial NOT NULL,
	tipo varchar(45) NOT NULL,
	CONSTRAINT tipo_imovel_pk PRIMARY KEY (id)
);

CREATE TABLE public.enderecos_imovel (
	id serial NOT NULL,
	logradouro varchar(100) NOT NULL,
	numero integer NOT NULL,
	complemento varchar(100) NULL,
	cep integer NOT NULL,
	cidade varchar(45) NOT NULL,
	uf varchar(2) NOT NULL,
	CONSTRAINT endereco_imovel_pk PRIMARY KEY (id)
);

CREATE TABLE public.documentos_proprietario (
	id serial NOT NULL,
	cpf char(11) NOT NULL,
	rg char(9) NOT NULL,
	titulo_eleitoral char(12) NULL,
	CONSTRAINT proprietario_pk PRIMARY KEY (id)
);

CREATE TABLE public.proprietarios (
	id serial NOT NULL,
	nome varchar(100) NOT NULL,
	data_nascimento date NOT NULL,
	id_documentos_proprietario integer NOT NULL,
	estado_civil char(20) NOT NULL,
	data_compra date NOT NULL,
	profissao varchar(100) NOT NULL,
	CONSTRAINT proprietarios_pk PRIMARY KEY (id),
	CONSTRAINT proprietarios_fk FOREIGN KEY (id_documentos_proprietario) REFERENCES public.documentos_proprietario(id) ON DELETE CASCADE
);

CREATE TABLE public.gastos_imovel (
	id serial NOT NULL,
	conta_luz money NULL DEFAULT 0,
	conta_agua money NULL DEFAULT 0,
	condominio money NULL DEFAULT 0,
	propaganda_venda money NULL DEFAULT 0,
	CONSTRAINT gastos_imovel_pk PRIMARY KEY (id)
);

CREATE TABLE public.financiamentos (
	id serial NOT NULL,
	banco integer NOT NULL,
	quantidade_parcelas integer NOT NULL,
	porcetagem_entrada double precision NOT NULL
);
ALTER TABLE public.financiamentos ADD CONSTRAINT financiamentos_pk PRIMARY KEY (id);

CREATE TABLE public.imoveis (
	id serial NOT NULL,
	id_tipo integer NOT NULL,
	id_endereco integer NOT NULL,
	id_proprietario integer NOT NULL,
	id_gastos integer NOT NULL,
	CONSTRAINT imoveis_pk PRIMARY KEY (id),
	CONSTRAINT imoveis_fk FOREIGN KEY (id_tipo) REFERENCES public.tipos_imovel(id),
	CONSTRAINT imoveis_fk_1 FOREIGN KEY (id_endereco) REFERENCES public.enderecos_imovel(id),
	CONSTRAINT imoveis_fk_2 FOREIGN KEY (id_proprietario) REFERENCES public.proprietarios(id),
	CONSTRAINT imoveis_fk_3 FOREIGN KEY (id_gastos) REFERENCES public.gastos_imovel(id)
);

CREATE TABLE public.vendas (
	id serial NOT NULL,
	valor_imovel double precision NOT NULL,
	id_cliente integer NOT NULL,
	id_financiamento integer NULL,
	id_imovel integer NOT NULL,
	CONSTRAINT vendas_pk PRIMARY KEY (id),
	CONSTRAINT vendas_fk FOREIGN KEY (id_cliente) REFERENCES public.proprietarios(id),
	CONSTRAINT vendas_fk_1 FOREIGN KEY (id_financiamento) REFERENCES public.financiamentos(id),
	CONSTRAINT vendas_fk_2 FOREIGN KEY (id_imovel) REFERENCES public.imoveis(id)
);
