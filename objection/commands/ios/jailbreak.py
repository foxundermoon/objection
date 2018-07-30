from objection.state.connection import state_connection
from objection.utils.frida_transport import FridaRunner
from objection.utils.templates import ios_hook


def disable(args: list = None) -> None:
    """
        Attempts to disable jailbreak detection.

        :param args:
        :return:
    """

    api = state_connection.get_api()
    api.ios_jailbreak_disable()


def simulate(args: list = None) -> None:
    """
        Attempts to simulate a Jailbroken environment

        :param args:
        :return:
    """

    hook = ios_hook('jailbreak/simulate')

    runner = FridaRunner(hook=hook)
    runner.run_as_job(name='simulate-jailbroken-environment')
