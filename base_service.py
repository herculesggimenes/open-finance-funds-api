import pandas as pd
import numpy as np

class BaseService:
    #init
    def __init__(self):
        #Fundos CVM 555
        df_fundos = pd.read_csv('cad_fi.csv',encoding='iso8859-1', sep=';')
        df_tipo_fundos = pd.read_csv('cad_tipos_fi.csv',encoding='utf-8', sep=';')
        #replace NaN with None
        df_fundos = df_fundos.where((pd.notnull(df_fundos)), '')
        df_fundos = df_fundos.replace({np.nan: ''})
        columns = {
            'ADMIN': 'administrador',
            'AUDITOR': 'auditor',
            'CD_CVM': 'codigoCVM',
            'CLASSE': 'classe',
            'CNPJ_ADMIN': 'cnpjAdministrador',
            'CNPJ_AUDITOR': 'cnpjAuditor',
            'CNPJ_CONTROLADOR': 'cnpjControlador',
            'CNPJ_CUSTODIANTE': 'cnpjCustodiante',
            'CNPJ_FUNDO': 'cnpjFundo',
            'CONDOM': 'formaCondominio', #Aberto/Fechado
            'CONTROLADOR': 'controlador',
            'CPF_CNPJ_GESTOR': 'cpfCnpjGestor',
            'CUSTODIANTE': 'custodiante',
            'DENOM_SOCIAL': 'denominacaoSocial',
            'DIRETOR': 'diretor',
            'DT_CANCEL': 'dataCancelamento',
            'DT_CONST': 'dataConstituicao',
            'DT_FIM_EXERC': 'dataFimExercicio',
            'DT_INI_ATIV': 'dataInicioAtividade',
            'DT_INI_EXERC': 'dataInicioExercicio',
            'DT_INI_CLASSE': 'dataInicioClasse',
            'DT_INI_EXERC': 'dataInicioExercicio',
            'DT_INI_SIT': 'dataInicioSituacao',
            'DT_PATRIM_LIQ': 'dataPatrimonioLiquido',
            'DT_REG': 'dataRegistro',
            'ENTID_INVEST': 'entidadeInvestimento', #Indica se o Fundo é entidade de Investimento
            'FUNDO_COTAS': 'fundoCotas', #Indica se o Fundo é de Cotas
            'FUNDO_EXCLUSIVO:': 'fundoExclusivo', #Indica se o Fundo é Exclusivo
            'GESTOR': 'gestor', #Nome do Gestor
            'INF_TAXA_ADM': 'informacaoTaxaAdministracao', #Indica se o Fundo possui informação de taxa de administração
            'INF_TAXA_PERFM': 'informacaoTaxaPerformance', #Indica se o Fundo possui informação de taxa de performance
            'INVEST_QUALIF': 'investimentoQualificado', #Indica se o Fundo é investimento qualificado
            'INVEST_PROF': 'investidorProfissional', #Indica se o Fundo é investimento qualificado
            'PF_PJ_GESTOR': 'pfPjGestor', #Indica se o Gestor é Pessoa Física ou Jurídica
            'RENTAB_FUNDO': 'rentabilidadeFundo', #Forma de rentabilidade do fundo
            'SIT': 'situacao', #Situação do Fundo
            'TAXA_ADM': 'taxaAdministracao', #Taxa de administração do Fundo
            'TAXA_PERFM': 'taxaPerformance', #Taxa de performance do Fundo
            'TP_FUNDO': 'tipoFundo', #Tipo de Fundo
            'TRIB_LPRAZO': 'tributacaoLongoPrazo', #Indica se o Fundo é tributado em longo prazo
            'VL_PATRIM_LIQ': 'valorPatrimonioLiquido', #Valor do Patrimônio Líquido do Fundo

            }
        df_fundos.rename(columns=columns, inplace=True)
        self._df_fundos = df_fundos
        self._df_tipo_fundos = df_tipo_fundos

    def get_tipos_fundos(self):
        return self._df_fundos.drop_duplicates(subset='tipoFundo', keep='first').tipoFundo.tolist()

    def get_classes_fundo(self):
        return self._df_fundos.drop_duplicates(subset='classe', keep='first').classe.tolist()

    def get_fundos(self):
        return self._df_fundos


    def get_fundos_por_tipo_fundo(self, tipo_fundo:str):
        # get distinct tipoFundo 
        return self._df_fundos[self._df_fundos['tipoFundo'] == tipo_fundo]

    def get_fundos_por_classe(self, classe:str):
         return self._df_fundos[self._df_fundos['classe'] == classe]

    def get_fundo_by_cnpj(self, cnpj:str):
        return self._df_fundos[self._df_fundos['cnpjFundo'] == cnpj]


    
    
    
    