/*App.js*/
import './App.css';
import Multiplicar from './components/Multiplicar';
import Titulo from './components/Titulo';
import Frase from './components/Frase';
import Imagem from './components/Imagem';

function App() {
  return (
    <div className="pagina">
      <Titulo />
      <p>{Multiplicar(5, 4)}</p>
      <Imagem />
      <Frase texto="Linha de mensagem 01" />
      <Frase texto="Linha de mensagem 02" />
      <Frase texto="Linha de mensagem 03" />
    </div>
  );
}

export default App;