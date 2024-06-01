import React, { useState } from 'react';
import { MultiTenantContextProvider } from './MultiTenantContext';

function App({ Component, pageProps }) {
  const [currentTenant, setCurrentTenant] = useState('default');

  return (
    <MultiTenantContextProvider value={{ currentTenant, setCurrentTenant }}>
      <Component {...pageProps} />
    </MultiTenantContextProvider>
  );
}

export default App;
