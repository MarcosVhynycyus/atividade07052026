from init import initialize_database
from src.modules.cinema.cinema_controller import CinemaController
from src.modules.cinema.cinema_repository import CinemaRepository
from src.modules.cinema.cinema_service import CinemaService
from src.modules.cinema.cinema_view import CinemaView
from src.modules.filme.filme_controller import FilmeController
from src.modules.filme.filme_repository import FilmeRepository
from src.modules.filme.filme_service import FilmeService
from src.modules.filme.filme_view import FilmeView
from src.modules.publico.publico_controller import PublicoController
from src.modules.publico.publico_repository import PublicoRepository
from src.modules.publico.publico_service import PublicoService
from src.modules.publico.publico_view import PublicoView
from src.modules.relatorio.relatorio_controller import RelatorioController
from src.modules.relatorio.relatorio_repository import RelatorioRepository
from src.modules.relatorio.relatorio_service import RelatorioService
from src.modules.relatorio.relatorio_view import RelatorioView
from src.modules.sessao.sessao_controller import SessaoController
from src.modules.sessao.sessao_repository import SessaoRepository
from src.modules.sessao.sessao_service import SessaoService
from src.modules.sessao.sessao_view import SessaoView
from src.modules.usuario.usuario_controller import UsuarioController
from src.modules.usuario.usuario_repository import UsuarioRepository
from src.modules.usuario.usuario_service import UsuarioService
from src.modules.usuario.usuario_view import UsuarioView
from src.pages.admin_menu import AdminMenuPage
from src.pages.login import LoginPage
from src.pages.menu import MenuPage


class App:
    def __init__(self):
        sessao_repository = SessaoRepository()
        sessao_service = SessaoService(sessao_repository)
        sessao_controller = SessaoController(sessao_service)

        publico_repository = PublicoRepository()
        publico_service = PublicoService(publico_repository)
        publico_controller = PublicoController(publico_service)

        relatorio_repository = RelatorioRepository()
        relatorio_service = RelatorioService(relatorio_repository)
        relatorio_controller = RelatorioController(relatorio_service)

        cinema_repository = CinemaRepository()
        cinema_service = CinemaService(cinema_repository)
        cinema_controller = CinemaController(cinema_service)

        filme_repository = FilmeRepository()
        filme_service = FilmeService(filme_repository)
        filme_controller = FilmeController(filme_service)

        usuario_repository = UsuarioRepository()
        usuario_service = UsuarioService(usuario_repository)
        usuario_controller = UsuarioController(usuario_service)

        self.login = LoginPage(
            usuario_controller=usuario_controller,
            usuario_view=UsuarioView(),
        )

        self.menu = MenuPage(
            sessao_controller=sessao_controller,
            sessao_view=SessaoView(),
            publico_controller=publico_controller,
            publico_view=PublicoView(),
            relatorio_controller=relatorio_controller,
            relatorio_view=RelatorioView(),
            cinema_controller=cinema_controller,
            cinema_view=CinemaView(),
            filme_controller=filme_controller,
            filme_view=FilmeView(),
        )
        self.admin_menu = AdminMenuPage(
            sessao_controller=sessao_controller,
            sessao_view=SessaoView(),
            publico_controller=publico_controller,
            publico_view=PublicoView(),
            relatorio_controller=relatorio_controller,
            relatorio_view=RelatorioView(),
            cinema_controller=cinema_controller,
            cinema_view=CinemaView(),
            filme_controller=filme_controller,
            filme_view=FilmeView(),
        )

    def run(self):
        initialize_database()
        usuario = self.login.exibir()
        if not usuario:
            return

        if usuario["perfil"] == "admin":
            self.admin_menu.exibir(usuario)
        else:
            self.menu.exibir(usuario)
