# Sistema de Pesquisa com Interação do Usuário
# Usando todos os conceitos de listas aprendidos

from collections import deque

class SistemaPesquisa:
    """
    Sistema interativo de pesquisa que utiliza todos os conceitos de listas:
    - Adição de elementos
    - Remoção de elementos
    - Listas como filas (FIFO)
    - Listas como pilhas (LIFO)
    """
    
    def __init__(self):
        self.resultados_pesquisa = []           # Lista principal de pesquisa
        self.historico_pesquisas = []           # Pilha de histórico (LIFO)
        self.fila_pesquisas_pendentes = deque() # Fila de pendentes (FIFO)
        self.pesquisas_favoritas = []           # Lista de favoritos
    
    def adicionar_resultado(self, termo):
        """
        Adiciona um resultado à lista de pesquisa.
        Demonstra: append() e extend()
        """
        if termo.strip() == "":
            print("❌ Termo de pesquisa não pode estar vazio!\n")
            return False
        
        if termo in self.resultados_pesquisa:
            print(f"⚠️  '{termo}' já está na lista de pesquisa!\n")
            return False
        
        self.resultados_pesquisa.append(termo)
        self.historico_pesquisas.append(termo)  # Adiciona ao histórico também
        print(f"✓ '{termo}' adicionado à pesquisa com sucesso!\n")
        return True
    
    def adicionar_multiplos_resultados(self, termos):
        """
        Adiciona múltiplos resultados de uma vez.
        Demonstra: extend()
        """
        novos_termos = [t for t in termos if t not in self.resultados_pesquisa and t.strip() != ""]
        if novos_termos:
            self.resultados_pesquisa.extend(novos_termos)
            self.historico_pesquisas.extend(novos_termos)
            print(f"✓ {len(novos_termos)} termo(s) adicionado(s) com sucesso!\n")
            return True
        else:
            print("❌ Nenhum termo novo para adicionar!\n")
            return False
    
    def remover_resultado(self, termo):
        """
        Remove um resultado da lista.
        Demonstra: remove()
        """
        try:
            self.resultados_pesquisa.remove(termo)
            print(f"✓ '{termo}' removido da pesquisa!\n")
            return True
        except ValueError:
            print(f"❌ '{termo}' não encontrado na lista!\n")
            return False
    
    def remover_ultimo_resultado(self):
        """
        Remove o último resultado adicionado.
        Demonstra: pop() como pilha
        """
        if len(self.resultados_pesquisa) > 0:
            removido = self.resultados_pesquisa.pop()
            print(f"✓ Último resultado '{removido}' removido!\n")
            return removido
        else:
            print("❌ Nenhum resultado para remover!\n")
            return None
    
    def inserir_resultado(self, termo, posicao):
        """
        Insere um resultado em uma posição específica.
        Demonstra: insert()
        """
        if termo in self.resultados_pesquisa:
            print(f"⚠️  '{termo}' já está na lista!\n")
            return False
        
        if posicao < 0 or posicao > len(self.resultados_pesquisa):
            print(f"❌ Posição inválida! (0-{len(self.resultados_pesquisa)})\n")
            return False
        
        self.resultados_pesquisa.insert(posicao, termo)
        print(f"✓ '{termo}' inserido na posição {posicao}!\n")
        return True
    
    def buscar_resultado(self, termo):
        """
        Busca um resultado na lista.
        Demonstra: uso de 'in' e index()
        """
        if termo in self.resultados_pesquisa:
            indice = self.resultados_pesquisa.index(termo)
            print(f"✓ '{termo}' encontrado na posição {indice}!\n")
            return indice
        else:
            print(f"❌ '{termo}' não encontrado!\n")
            return None
    
    def adicionar_aos_favoritos(self, termo):
        """
        Adiciona um resultado aos favoritos.
        Demonstra: append() para favoritos
        """
        if termo not in self.resultados_pesquisa:
            print(f"❌ '{termo}' não está na lista de pesquisa!\n")
            return False
        
        if termo in self.pesquisas_favoritas:
            print(f"⚠️  '{termo}' já é favorito!\n")
            return False
        
        self.pesquisas_favoritas.append(termo)
        print(f"⭐ '{termo}' adicionado aos favoritos!\n")
        return True
    
    def remover_dos_favoritos(self, termo):
        """
        Remove um resultado dos favoritos.
        Demonstra: remove()
        """
        try:
            self.pesquisas_favoritas.remove(termo)
            print(f"✓ '{termo}' removido dos favoritos!\n")
            return True
        except ValueError:
            print(f"❌ '{termo}' não está nos favoritos!\n")
            return False
    
    def enfileirar_pesquisa_pendente(self, termo):
        """
        Enfileira uma pesquisa para processar depois.
        Demonstra: FIFO (fila com append e popleft)
        """
        self.fila_pesquisas_pendentes.append(termo)
        print(f"✓ '{termo}' adicionado à fila de pendentes!\n")
    
    def processar_proxima_pesquisa_pendente(self):
        """
        Processa a próxima pesquisa pendente.
        Demonstra: FIFO com popleft()
        """
        if len(self.fila_pesquisas_pendentes) > 0:
            termo = self.fila_pesquisas_pendentes.popleft()
            print(f"✓ Processando pesquisa pendente: '{termo}'\n")
            return termo
        else:
            print("❌ Nenhuma pesquisa pendente!\n")
            return None
    
    def voltar_pesquisa_anterior(self):
        """
        Volta para a pesquisa anterior no histórico.
        Demonstra: LIFO (pilha com append e pop)
        """
        if len(self.historico_pesquisas) > 1:
            self.historico_pesquisas.pop()  # Remove atual
            anterior = self.historico_pesquisas[-1]
            print(f"← Voltando para: '{anterior}'\n")
            return anterior
        else:
            print("❌ Nenhuma pesquisa anterior no histórico!\n")
            return None
    
    def listar_resultados(self):
        """
        Lista todos os resultados de pesquisa.
        Demonstra: iteração sobre listas
        """
        if len(self.resultados_pesquisa) == 0:
            print("❌ Nenhum resultado de pesquisa!\n")
            return
        
        print("\n" + "="*50)
        print("RESULTADOS DE PESQUISA")
        print("="*50)
        for i, resultado in enumerate(self.resultados_pesquisa):
            marcador = "⭐" if resultado in self.pesquisas_favoritas else "  "
            print(f"{i:2d}. {marcador} {resultado}")
        print("="*50 + "\n")
    
    def listar_historico(self):
        """
        Lista o histórico de pesquisas.
        Demonstra: pilha (LIFO)
        """
        if len(self.historico_pesquisas) == 0:
            print("❌ Histórico vazio!\n")
            return
        
        print("\n" + "="*50)
        print("HISTÓRICO DE PESQUISAS (Mais recente → Mais antigo)")
        print("="*50)
        for i, pesquisa in enumerate(reversed(self.historico_pesquisas)):
            print(f"{i+1}. {pesquisa}")
        print("="*50 + "\n")
    
    def listar_pendentes(self):
        """
        Lista as pesquisas pendentes.
        Demonstra: fila (FIFO)
        """
        if len(self.fila_pesquisas_pendentes) == 0:
            print("❌ Nenhuma pesquisa pendente!\n")
            return
        
        print("\n" + "="*50)
        print("PESQUISAS PENDENTES (Primeira a processar)")
        print("="*50)
        for i, pesquisa in enumerate(self.fila_pesquisas_pendentes):
            print(f"{i+1}. {pesquisa}")
        print("="*50 + "\n")
    
    def listar_favoritos(self):
        """
        Lista os favoritos.
        Demonstra: uso de listas
        """
        if len(self.pesquisas_favoritas) == 0:
            print("❌ Nenhum favorito salvo!\n")
            return
        
        print("\n" + "="*50)
        print("PESQUISAS FAVORITAS ⭐")
        print("="*50)
        for i, fav in enumerate(self.pesquisas_favoritas):
            print(f"{i+1}. {fav}")
        print("="*50 + "\n")
    
    def limpar_tudo(self):
        """
        Limpa todos os dados.
        Demonstra: clear()
        """
        self.resultados_pesquisa.clear()
        self.historico_pesquisas.clear()
        self.fila_pesquisas_pendentes.clear()
        self.pesquisas_favoritas.clear()
        print("✓ Todos os dados foram limpos!\n")
    
    def mostrar_menu(self):
        """
        Exibe o menu interativo.
        """
        print("\n" + "="*50)
        print("SISTEMA DE PESQUISA - MENU")
        print("="*50)
        print("1. Adicionar resultado")
        print("2. Adicionar múltiplos resultados")
        print("3. Listar resultados")
        print("4. Buscar resultado")
        print("5. Inserir resultado em posição específica")
        print("6. Remover resultado")
        print("7. Remover último resultado")
        print("8. Adicionar aos favoritos")
        print("9. Remover dos favoritos")
        print("10. Listar favoritos")
        print("11. Ver histórico (PILHA)")
        print("12. Voltar pesquisa anterior")
        print("13. Ver pesquisas pendentes (FILA)")
        print("14. Enfileirar pesquisa pendente")
        print("15. Processar próxima pesquisa pendente")
        print("16. Limpar tudo")
        print("0. Sair")
        print("="*50 + "\n")
    
    def executar(self):
        """
        Executa o programa interativo.
        """
        print("\n🔍 BEM-VINDO AO SISTEMA DE PESQUISA COM LISTAS!")
        print("Este programa demonstra todos os conceitos de listas em Python\n")
        
        while True:
            self.mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                termo = input("Digite o termo de pesquisa: ").strip()
                self.adicionar_resultado(termo)
            
            elif opcao == "2":
                termos_str = input("Digite termos separados por vírgula: ").strip()
                if termos_str:
                    termos = [t.strip() for t in termos_str.split(",")]
                    self.adicionar_multiplos_resultados(termos)
            
            elif opcao == "3":
                self.listar_resultados()
            
            elif opcao == "4":
                termo = input("Digite o termo a buscar: ").strip()
                self.buscar_resultado(termo)
            
            elif opcao == "5":
                self.listar_resultados()
                termo = input("Digite o termo a inserir: ").strip()
                try:
                    posicao = int(input("Digite a posição (0 para início): ").strip())
                    self.inserir_resultado(termo, posicao)
                except ValueError:
                    print("❌ Posição inválida!\n")
            
            elif opcao == "6":
                termo = input("Digite o termo a remover: ").strip()
                self.remover_resultado(termo)
            
            elif opcao == "7":
                self.remover_ultimo_resultado()
            
            elif opcao == "8":
                self.listar_resultados()
                termo = input("Digite o termo a adicionar aos favoritos: ").strip()
                self.adicionar_aos_favoritos(termo)
            
            elif opcao == "9":
                self.listar_favoritos()
                termo = input("Digite o termo a remover dos favoritos: ").strip()
                self.remover_dos_favoritos(termo)
            
            elif opcao == "10":
                self.listar_favoritos()
            
            elif opcao == "11":
                self.listar_historico()
            
            elif opcao == "12":
                self.voltar_pesquisa_anterior()
            
            elif opcao == "13":
                self.listar_pendentes()
            
            elif opcao == "14":
                termo = input("Digite o termo para enfileirar: ").strip()
                if termo:
                    self.enfileirar_pesquisa_pendente(termo)
            
            elif opcao == "15":
                self.processar_proxima_pesquisa_pendente()
            
            elif opcao == "16":
                confirmacao = input("Tem certeza? (S/N): ").strip().lower()
                if confirmacao == "s":
                    self.limpar_tudo()
            
            elif opcao == "0":
                print("\n👋 Até logo! Obrigado por usar o Sistema de Pesquisa!\n")
                break
            
            else:
                print("❌ Opção inválida! Tente novamente.\n")


# Executar o programa
if __name__ == "__main__":
    sistema = SistemaPesquisa()
    sistema.executar()