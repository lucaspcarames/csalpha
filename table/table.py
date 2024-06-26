
from table.abstract_table import TableBase
from circuit.circuit import Circuit
from circuit.abstract_circuit import CircuitBase
import pandas as pd
from typing import Any
import hashlib
import time


class Table(TableBase):
    """
    Class that presents consolidated data via circuit

    *last level of interface with the user*
    *The table is a composition of circuits*

    Attributes
    ----------
    _base_df : pd.DataFrame
        DataFrame that stores the consolidated data via circuit.
    
    Methods
    -------
    create_table(**kwargs) -> pd.DataFrame:
        Consolidates the input and validated data into a pd.DataFrame.
    """

    def __init__(self):
        self.id_table: str = self._generate_id_table()

        self._dict_table: dict = {}

        self._dataframe_table: pd.DataFrame = pd.DataFrame()

    def insert_circuit(self, circuit: Circuit) -> None:
        self._dict_table.update({circuit.circuit_id: circuit})


    def remove_circuit(self, circuit_remove: Any) -> None:
        if isinstance(circuit_remove, Circuit):
            circuit_id = circuit_remove.circuit_id
        else:
            circuit_id = circuit_remove

        try:
            self._dict_table.pop(circuit_id)
        
        except KeyError as e:
            print("Circuit not found.", e)


    def show_table(self, format: str = 'standard') -> Any:
        """
        format must be either 'pandas' or 'standard'
        """
        if format=='standard':
            _dic_show = {}
            for k, v in self._dict_table.items():
                _dic_show.update({k: v.get_launches()})
            return _dic_show

        elif format=='pandas':
            app_list = []

            for k, v in self._dict_table.items():
                if v.is_closed():
                    app_list.append(v.show_dataframe_circuit())
                else:
                    v.circuit_closed(True)
                    app_list.append(v.show_dataframe_circuit())

            return pd.concat(app_list)

        


    def _generate_id_table(self, id_tabela: Any = 'auto') -> str:
        """
        Generates a unique ID for the table using SHA-1.

        Parameters
        ----------
        id_tabela : Any
            Defines the table ID. If "auto", the ID will be generated
            from SHA-1 hash. By default, "auto".

        Returns
        -------
        str
            Unique ID generated for the table.
        """
        if id_tabela == 'auto':
            seed = str(time.time()) + "36NOYMrLnmlextec"
            id_ = hashlib.sha1(seed.encode()).hexdigest()[:10]
        else: 
            id_ = str(seed)
        
        
        return id_
