export const 後端網址 = 'https://dbkaxabu.xn--v0qr21b.xn--kpry57d/';

export const ImtongBangtsi = (pianho, gi) => {
  if(gi == 'Kaxabu'){
    gi = '噶哈巫'
  }
	return `${後端網址}聽?語詞編號=${pianho}&內容=${gi}`
}

export const TshaBangTshi = () => `${後端網址}查`