ALTER TABLE public.gastos_imovel ALTER COLUMN conta_luz TYPE numeric USING conta_luz::numeric;
ALTER TABLE public.gastos_imovel ALTER COLUMN conta_agua TYPE numeric USING conta_agua::numeric;
ALTER TABLE public.gastos_imovel ALTER COLUMN condominio TYPE numeric USING condominio::numeric;
ALTER TABLE public.gastos_imovel ALTER COLUMN propaganda_venda TYPE numeric USING propaganda_venda::numeric;
