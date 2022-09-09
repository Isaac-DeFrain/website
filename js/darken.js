console.log('here!')

const portfolioItems = document.querySelectorAll('.portfolio-item-wrapper')

portfolioItems.forEach(item => {
  item.addEventListener('mouseover', () => {
    console.log(item.childNodes[1].classList)
    item.childNodes[1].classList.add('.img-darken');
  })

  item.addEventListener('mouseout', () => {
    item.childNodes[1].classList.remove('.img-darken');
  })
})
