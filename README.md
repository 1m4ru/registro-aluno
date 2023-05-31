# registro-aluno
Trabalho da faculdade com registro de aluno.
Cadastro de Alunos
Este documento contém informações sobre a aplicação "Cadastro de Alunos", que é um sistema projetado para gerenciar informações dos alunos em uma instituição de ensino. O sistema possui funcionalidades que permitem o cadastro de novos alunos, o gerenciamento de informações pessoais, o registro de notas e frequência, a consulta de informações e a geração de relatórios e estatísticas.

Funcionalidades
A seguir estão listadas as principais funcionalidades do sistema "Cadastro de Alunos":

Cadastro de Novos Alunos: O sistema permite o registro de novos alunos, incluindo informações pessoais como nome completo, data de nascimento, endereço, contato e outras informações relevantes. Cada aluno é atribuído um identificador único, como um número de matrícula, para facilitar sua identificação no sistema.

Gerenciamento de Informações Pessoais: É possível editar e atualizar as informações pessoais dos alunos, como endereço, contato de emergência, entre outros. O sistema também oferece campos adicionais para registrar informações complementares, como fotografia do aluno, documentos relacionados e histórico familiar.

Registro de Notas: O sistema permite o registro de notas dos alunos em diferentes disciplinas ou matérias. É importante definir a estrutura das notas, como a escala de avaliação (por exemplo, de 0 a 10) e o peso de cada nota na média final.

Registro de Frequência: O sistema permite o registro da frequência dos alunos nas aulas. Pode ser utilizado um sistema de presença, como marcação de presença em sala de aula ou registro de entrada e saída.

Consulta de Informações: O sistema fornece uma interface de consulta para que os usuários possam obter informações sobre os alunos, como notas, frequência, informações pessoais, entre outros. As consultas podem ser filtradas por critérios, como nome do aluno ou turma.

Relatórios e Estatísticas: O sistema pode gerar relatórios e estatísticas agregadas, como média geral da turma, índice de presença, entre outros. Também exibe uma tela com a porcentagem de aprovações, média das notas por turma e quantidade de alunos por turma.

Requisitos
Antes de começar a instalação, verifique se você possui os seguintes requisitos em sua máquina:

IDE de desenvolvimento, como VScode.
Python instalado.
Django instalado.
Instalação
Siga as etapas abaixo para instalar e executar a aplicação "Cadastro de Alunos":

Faça o download dos arquivos da aplicação "Cadastro de Alunos".
Abra um terminal e navegue até o diretório onde os arquivos da aplicação estão localizados.
Crie um ambiente virtual executando o seguinte comando:

python -m venv nome_do_ambiente

Ative o ambiente virtual:
No Windows:
nome_do_ambiente\Scripts\activate

No macOS/Linux:
source nome_do_ambiente/bin/activate

Instale as dependências do Django executando o seguinte comando:
pip install django

Importe o banco de dados fornecido ou crie um novo banco de dados vazio. Para criar um novo banco de dados, você pode usar o seguinte comando do Django:
python manage.py migrate

Configure as credenciais de acesso ao banco de dados no arquivo de configuração correspondente, localizado em nome_do_projeto/settings.py.
Inicie a aplicação executando o seguinte comando:

python manage.py runserver

Abra um navegador e acesse http://localhost:8000 para verificar se a aplicação está funcionando corretamente.

Utilização
Após a instalação e execução da aplicação "Cadastro de Alunos", siga as instruções fornecidas pela interface do Django para utilizar as funcionalidades do sistema.

Autores
Maruan Moussa - Desenvolvedor front-end
Gustavo Correa - Designer/ Desenvolvedor front-end
Mauricio Cardoso Oliveira - Desenvolvedor back-end
Cristofer Cardoso Machado - Desenvolvedor back-end




